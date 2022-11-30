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

def add_inst(db: Session, user_id: int, key_text: str, message_id: int):
        if (user_id == None):
            raise ValidationError
        if (key_text == ''):
            raise ValidationError
        if (message_id == None or not isinstance(message_id, int)):
            raise ValidationError
        key_text = key_text.lower().strip()

        
        inst = Instruction(user_id=user_id, key_text=key_text, message_id=message_id)
        db.add(inst)
        db.commit()


