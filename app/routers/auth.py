from fastapi import HTTPException, APIRouter, APIRouter, Depends, status, Response
from sqlalchemy.orm import session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..import database, schemas, models, utils, oauth2

router=APIRouter(tags={'Autentification'})

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: session=Depends(database.get_db)): #OAuth2PasswordRequestForm sablona za login ima username i pwt bez emaila koji se uzima kao username

    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    



    #create token

    acces_token = oauth2.create_acces_token(data = {"user_id": user.id})

    #return token

    return {"access_token": acces_token, "token_type": "bearer"}

