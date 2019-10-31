import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Presets(Base):
    __tablename__='presets'
    id = Column(Integer, primary_key = True)
    descripcion = Column(String(250))
    tamMemoria = Column(Integer)
    sistOpMem = Column(Integer)
    fija_variable = Column(String(1))
    cant_part = Column(Integer)
    algoritmo_as = Column(Integer)
    algoritmo_pla = Column(Integer)

class Particiones(Base):
    __tablename__='particiones'
    id_part = Column(Integer, primary_key = True)
    batch = Column(String(50))
    tam_part = Column(Integer)
    dir_ini = Column(Integer)
    dir_fin = Column(Integer)

class Proceso(Base):
    __tablename__='proceso'
    id_proc = Column(Integer, primary_key =True)
    id_batch = Column(String(50), primary_key = True)
    tam_proc = Column(Integer)
    prioridad = Column(Integer)
    rafagaCPU = Column(String(50))
    tiempo_arribo = Column(Integer)

engine = create_engine('sqlite:///SistOp.db')

Base.metadata.create_all(engine)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
