from BD_connect import *
from datetime import datetime

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

        if (len(list(db.query(Instruction).filter(Instruction.user_id==user_id).where(Instruction.key_text==key_text))) > 0):
            raise ValueError
        
        inst = Instruction(user_id=user_id, key_text=key_text, message_id=message_id)
        db.add(inst)
        db.commit()

def del_inst(db: Session, id: int):
    if (id <=0):
        raise ValueError
    
    inst = db.query(Instruction).filter(Instruction.id==id)
    if (len(list(inst)) == 0):
        raise KeyError
        
    inst.delete(synchronize_session='evaluate')
    db.commit()


def add_notif(db: Session, user_id: int, notif_text: str, exec_datetime: DateTime):
    if (user_id == None):
            raise ValidationError
    if (notif_text == ''):
        raise ValidationError
    if (exec_datetime == None ):  # parse form datetime.strptime('30.11.22 17:22','%d.%m.%y %H:%M')
        raise ValidationError
    
    notif = Notification(user_id=user_id, notif_text=notif_text, exec_datetime=exec_datetime)
    db.add(notif)
    db.commit()

def get_notifs(db: Session, user_id: int, id: int = 0):
    if (user_id == None):
        raise ValidationError
    
    if (id > 0):
        items = db.query(Notification).filter(Notification.user_id==user_id).where(Notification.id==id)
        if (len(list(items)) != 1):
            raise KeyError
    else:
        items = db.query(Notification).filter(Notification.user_id==user_id)
        if (len(list(items)) == 0):
            raise ValueError
    return items

def update_notif(db: Session, user_id: int, id: int, new_notif_text: str = '', new_exec_datetime: DateTime = None):
    if (user_id == None or id <= 0):
        raise ValidationError
    
    if (new_notif_text == '' and new_exec_datetime == None):
        raise ValueError
    
    notif = db.query(Notification).filter(Notification.user_id==user_id).filter(Notification.id==id).\
        one()
    
    if (new_notif_text != ''):
        notif.notif_text = new_notif_text
    if (new_exec_datetime != None):
        notif.exec_datetime = new_exec_datetime
    
    db.commit()

