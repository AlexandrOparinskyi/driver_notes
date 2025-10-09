from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub

DIR_PATH = 'I18N/locales'


def create_translator_hub() -> TranslatorHub:
    return TranslatorHub(
        {'ru': ('ru', 'en'), 'en': 'en'},
        [
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    locale='ru',
                    filenames=[f'{DIR_PATH}/ru/general.ftl',
                               f'{DIR_PATH}/ru/start.ftl']),
            ),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en',
                    filenames=[f'{DIR_PATH}/en/general.ftl',
                               f'{DIR_PATH}/en/start.ftl',]),
            ),
        ],
        root_locale='en',
    )
