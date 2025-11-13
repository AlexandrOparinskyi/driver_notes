from datetime import datetime
from io import BytesIO
from html import unescape
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

from bot.utils import get_service_by_id


async def register_russian_fonts():
    """Регистрация русского шрифта"""
    try:
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
        return 'DejaVuSans'
    except:
        try:
            pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
            return 'Arial'
        except:
            return 'Helvetica'


def clean_html_text(text: str) -> str:
    """Очищает текст от HTML тегов и экранированных символов"""
    if not text:
        return ""
    # Убираем HTML теги
    text = re.sub(r'<[^>]+>', '', text)
    # Декодируем HTML entities
    text = unescape(text)
    return text.strip()


def safe_text(text: any) -> str:
    """Безопасное преобразование текста с очисткой HTML"""
    if text is None:
        return ""
    return clean_html_text(str(text))


async def create_single_service_record_pdf(
        service_record_id: int
) -> BytesIO:
    """
    Создает красивый PDF отчет по одной сервисной работе и возвращает BytesIO buffer
    """

    # Регистрируем русские шрифты
    font_name = await register_russian_fonts()

    # Получаем данные сервисной записи
    service_record = await get_service_by_id(service_record_id)

    if not service_record:
        raise ValueError(f"Сервисная запись с ID {service_record_id} не найдена")

    # Получаем данные автомобиля
    car = service_record.car

    # Создаем BytesIO buffer для PDF
    pdf_buffer = BytesIO()

    # Создаем документ в memory buffer
    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    # Создаем кастомные стили
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'RussianTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=18,
        spaceAfter=25,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4057'),
        borderPadding=(10, 10, 10, 10),
        borderColor=colors.HexColor('#3498DB'),
        borderWidth=1,
        backColor=colors.HexColor('#EBF5FB')
    )

    section_style = ParagraphStyle(
        'RussianSection',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=14,
        spaceAfter=12,
        textColor=colors.HexColor('#2C3E50'),
        leftIndent=5,
        borderLeft=3,
        borderColor=colors.HexColor('#E74C3C'),
        borderPadding=(5, 0, 0, 5)
    )

    normal_style = ParagraphStyle(
        'RussianNormal',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=10,
        spaceAfter=6,
        textColor=colors.HexColor('#2C3E50'),
        alignment=TA_JUSTIFY
    )

    footer_style = ParagraphStyle(
        'RussianFooter',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=8,
        spaceAfter=0,
        textColor=colors.HexColor('#7F8C8D'),
        alignment=TA_CENTER
    )

    # Содержимое документа
    story = []

    # Заголовок
    story.append(Paragraph("АКТ ВЫПОЛНЕННЫХ РАБОТ", title_style))
    story.append(Spacer(1, 15))

    # Блок информации об автомобиле
    story.append(Paragraph("ИНФОРМАЦИЯ ОБ АВТОМОБИЛЕ", section_style))

    car_info_data = [
        ["Название:", safe_text(car.name) or "Не указано"],
        ["Марка:", safe_text(car.mark) or "Не указана"],
        ["Модель:", safe_text(car.model) or "Не указана"],
        ["Год выпуска:", str(car.year) if car.year else "Не указан"],
        ["Цвет:", safe_text(car.color) or "Не указан"],
        ["Тип двигателя:", car.engine_type.value if car.engine_type else "Не указан"],
        ["Коробка передач:", car.transmission_type.value if car.transmission_type else "Не указан"],
        ["Пробег:", f"{car.mileage} км" if car.mileage else "Не указан"]
    ]

    car_table = Table(car_info_data, colWidths=[40 * mm, 120 * mm])
    car_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F8F9F9')),
        ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#FFFFFF')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2C3E50')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
    ]))
    story.append(car_table)
    story.append(Spacer(1, 20))

    # Основная информация о сервисной работе
    story.append(Paragraph("ИНФОРМАЦИЯ О РАБОТЕ", section_style))

    record_info_data = []
    if service_record.title:
        record_info_data.append(["Название работы:", safe_text(service_record.title)])

    if service_record.service_type:
        smile = service_record.service_type.get_smile()
        record_info_data.append(["Тип обслуживания:", f"{smile} {service_record.service_type.value}"])

    if service_record.service_date:
        record_info_data.append(["Дата выполнения:", service_record.service_date.strftime('%d.%m.%Y')])

    if service_record.service_center:
        record_info_data.append(["Сервисный центр:", safe_text(service_record.service_center)])

    total_cost = f"{service_record.total_price:.2f} руб." if service_record.total_price else "Не указана"
    record_info_data.append(["Общая стоимость:", total_cost])

    record_table = Table(record_info_data, colWidths=[45 * mm, 115 * mm])
    record_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F8F9F9')),
        ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#FFFFFF')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2C3E50')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
    ]))
    story.append(record_table)

    # Описание работы (если есть)
    if service_record.description:
        story.append(Spacer(1, 10))
        description_text = safe_text(service_record.description)
        if description_text:
            story.append(Paragraph("Описание работы:", section_style))
            story.append(Paragraph(description_text, normal_style))

    story.append(Spacer(1, 20))

    # Детализация работ
    if service_record.service_works:
        story.append(Paragraph("ВЫПОЛНЕННЫЕ РАБОТЫ", section_style))

        works_data = [['№', 'Наименование работы', 'Описание', 'Стоимость, руб.']]
        total_works_cost = 0

        for i, work in enumerate(service_record.service_works, 1):
            work_cost = work.price if work.price else 0
            total_works_cost += work_cost

            works_data.append([
                str(i),
                safe_text(work.name) or '-',
                safe_text(work.description) or '-',
                f"{work_cost:.2f}" if work_cost else '-'
            ])

        # Добавляем итого по работам как отдельную строку
        works_data.append(['', '', 'ИТОГО по работам:', f'{total_works_cost:.2f}'])

        # Увеличиваем ширину колонок для работ
        works_table = Table(works_data, colWidths=[15 * mm, 70 * mm, 60 * mm, 35 * mm])
        works_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), font_name),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#F8F9F9')),
            ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E74C3C')),
            ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#F8F9F9')]),
        ]))
        story.append(works_table)
        story.append(Spacer(1, 20))

    # Детализация запчастей с увеличенной шириной колонок
    if service_record.service_parts:
        story.append(Paragraph("ИСПОЛЬЗОВАННЫЕ ЗАПЧАСТИ И МАТЕРИАЛЫ", section_style))

        parts_data = [['№', 'Наименование', 'Артикул', 'Кол-во', 'Цена за ед., руб.', 'Сумма, руб.']]
        total_parts_cost = 0

        for i, part in enumerate(service_record.service_parts, 1):
            part_cost = part.total_price if part.total_price else 0
            total_parts_cost += part_cost

            parts_data.append([
                str(i),
                safe_text(part.name) or '-',
                safe_text(part.part_number) or '-',
                f"{part.quantity}" if part.quantity else '-',
                f"{part.price_per_unit:.2f}" if part.price_per_unit else '-',
                f"{part_cost:.2f}" if part_cost else '-'
            ])

        # Добавляем итого по запчастям как отдельную строку
        parts_data.append(['', '', '', '', 'ИТОГО по запчастям:', f'{total_parts_cost:.2f}'])

        # Увеличиваем ширину колонок для запчастей - делаем таблицу шире
        parts_table = Table(parts_data, colWidths=[15 * mm, 60 * mm, 30 * mm, 20 * mm, 30 * mm, 30 * mm])
        parts_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), font_name),
            ('FONTSIZE', (0, 0), (-1, -1), 9),  # Увеличили шрифт для лучшей читаемости
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#F8F9F9')),
            ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#3498DB')),
            ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#F8F9F9')]),
        ]))
        story.append(parts_table)
        story.append(Spacer(1, 20))

    # Итоговая стоимость
    story.append(Paragraph("ИТОГОВАЯ СТАТИСТИКА", section_style))

    total_works_cost = sum(work.price if work.price else 0 for work in service_record.service_works)
    total_parts_cost = sum(part.total_price if part.total_price else 0 for part in service_record.service_parts)
    record_total = service_record.total_price if service_record.total_price else 0

    summary_data = [
        ["Статья расходов", "Сумма, руб."],
        ["Стоимость работ:", f"{total_works_cost:.2f}"],
        ["Стоимость запчастей:", f"{total_parts_cost:.2f}"],
        ["Общая стоимость по акту:", f"{record_total:.2f}"]
    ]

    summary_table = Table(summary_data, colWidths=[100 * mm, 40 * mm])
    summary_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#F8F9F9')),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#27AE60')),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(summary_table)

    story.append(Spacer(1, 25))

    # Футер с датой генерации
    footer_text = f"Акт сгенерирован автоматически: {datetime.now().strftime('%d.%m.%Y в %H:%M')}"
    story.append(Paragraph(footer_text, footer_style))

    # Создаем PDF в buffer
    doc.build(story)

    # Перемещаем указатель в начало buffer
    pdf_buffer.seek(0)

    return pdf_buffer