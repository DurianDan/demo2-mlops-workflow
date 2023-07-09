from sqlalchemy import Column, Integer, String, Float, Boolean
from .base import BaseSQLModel, Base


class NewProblem(Base):
    """help interact with a table in PostgreSQL server"""

    __tablename__ = "Data"
    id = Column(Integer, primary_key=True, index=True)
    # request_id =


class Prob1Table(BaseSQLModel):
    __tablename__ = "1.1.FraudDetection"

    feature1 = Column(String)
    feature2 = Column(String)
    feature3 = Column(Float)
    feature4 = Column(Integer)
    feature5 = Column(Float)
    feature6 = Column(Float)
    feature7 = Column(Integer)
    feature8 = Column(Float)
    feature9 = Column(Float)
    feature10 = Column(Float)
    feature11 = Column(Integer)
    feature12 = Column(Integer)
    feature13 = Column(Integer)
    label = Column(Boolean)
    feature14 = Column(Float)
    feature15 = Column(Float)
    feature16 = Column(Float)


class Prob2Table(BaseSQLModel):
    __tablename__ = "1.2.CreditRiskPrediction"

    feature1 = Column(String)
    feature2 = Column(Float)
    feature3 = Column(String)
    feature4 = Column(String)
    feature5 = Column(Float)
    feature6 = Column(String)
    feature7 = Column(String)
    feature8 = Column(Float)
    feature9 = Column(String)
    feature10 = Column(String)
    feature11 = Column(Float)
    feature12 = Column(String)
    feature13 = Column(Float)
    feature14 = Column(String)
    feature15 = Column(String)
    feature16 = Column(Float)
    feature17 = Column(String)
    feature18 = Column(Float)
    feature19 = Column(String)
    feature20 = Column(String)
    label = Column(Boolean)
