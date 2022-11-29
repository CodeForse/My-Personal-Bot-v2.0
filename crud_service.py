from BD_connect import *

def get_instructions_by_user_id(db: Session, user_id: int, key_text: str = '') -> list[Instruction]:
    if (user_id == None):
        raise ValidationError
    
    if (key_text == ''):
        items = db.query(Instruction).filter(Instruction.user_id==user_id).all()
    else:
        items = db.query(Instruction).filter(Instruction.user_id==user_id).where(Instruction.key_text==key_text).all()
    
    if (len(items) == 0 or len(items) > 1):
        raise KeyError
    return items


with Session(engine) as db:
    items = get_instructions_by_user_id(db=db, user_id=687088043, key_text='as')
    print(items)