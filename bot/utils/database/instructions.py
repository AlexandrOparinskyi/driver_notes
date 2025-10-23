from sqlalchemy import select

from database import Instruction, get_async_session, LocaleTypeEnum


async def get_instruction_by_locale(locale: str) -> list[Instruction]:
    async with get_async_session() as session:
        return await session.scalars(select(Instruction).where(
            Instruction.locale == locale.upper()
        ))


async def get_instruction_by_id(instr_id: int) -> Instruction:
    async with get_async_session() as session:
        return await session.scalar(select(Instruction).where(
            Instruction.id == instr_id
        ))
