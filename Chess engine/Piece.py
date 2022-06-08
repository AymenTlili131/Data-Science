# piece motion bitboard 
# piece attack bitboard
# piece attackers
# piece promotion check castling
# piece preferred position np.array :eval
# piece preferred position update method for learning
from bitboards import bitboard
import numpy as np


class Pawn() :  #finish attackers dict /promotion/ en passant
    def __init__(self,color :int):
        self.initial_bb=bitboard()
        self.position_bb=bitboard()
        self.motion_bb=bitboard()
        self.attack_bb=bitboard()
        self.color=color             #{0:"W",1:"B"}
        self.enpassant_atk=False
        self.promotion=False
        self.value=0        #TO DO
        self.valueTable=0   #TO DO
        self.Letter= "P"  if self.color==0 else "p" 
        self.symbol= "♙" if self.color==0 else "♟︎"
        if color==0 :
            for i in range(8,16):
                self.initial_bb.setBitHot(i)
        if color==1:
            for i in range(48,56):
                self.initial_bb.setBitHot(i)
        self.position_bb=self.initial_bb
        self.value=0
        self.tactical_value=0
        self.table_list=None



class Rook():
    def __init__(self,color :int):
        self.color=color             #{0:"W",1:"B"}
        self.initial_bb=bitboard()
        self.position_bb=bitboard()
        self.motion_bb=bitboard()
        self.attack_bb=bitboard()
        self.castling_rights=[1,1]   # 1:True on Queen side 1:True on King side
        if (self.color==0):
            self.initial_bb.setBitHot(0)
            self.initial_bb.setBitHot(7)
        elif (self.color==1):
            self.initial_bb.setBitHot(56)
            self.initial_bb.setBitHot(63)
        self.position_bb=self.initial_bb
        self.Letter= "R"  if self.color==0 else "r" 
        self.symbol= "♖" if self.color==0 else "♜" 
        self.value=0
        self.tactical_value=0
        self.table_list=None


class Knight():               
    def __init__(self,color :int):
        self.color=color             #{0:"W",1:"B"}
        self.initial_bb=bitboard()
        self.position_bb=bitboard()
        self.motion_bb=bitboard()
        self.attack_bb=bitboard()
        if (self.color==0):
            self.initial_bb.setBitHot(1)
            self.initial_bb.setBitHot(6)
        elif (self.color==1):
            self.initial_bb.setBitHot(57)
            self.initial_bb.setBitHot(62)
        self.position_bb=self.initial_bb
        self.Letter= "N"  if self.color==0 else "n" 
        self.symbol= "♘" if self.color==0 else "♞" 
        self.value=0
        self.tactical_value=0
        self.table_list=None



class Bishop():
    def __init__(self,color :int):
        self.color=color             #{0:"W",1:"B"}
        self.initial_bb=bitboard()
        self.position_bb=bitboard()
        self.motion_bb=bitboard()
        self.attack_bb=bitboard()
        if (self.color==0):
            self.initial_bb.setBitHot(2)
            self.initial_bb.setBitHot(5)
        elif self.color==1 :
            self.initial_bb.setBitHot(58)
            self.initial_bb.setBitHot(61)
        self.position_bb=self.initial_bb
        self.Letter= "B"  if self.color==0 else "b" 
        self.symbol= "♗" if self.color==0 else "♝"
        self.value=0
        self.tactical_value=0 
        self.table_list=None


class Queen():
    def __init__(self,color :int):
        self.color=color             #{0:"W",1:"B"}
        self.initial_bb=bitboard()
        self.position_bb=bitboard()
        self.motion_bb=bitboard()
        self.attack_bb=bitboard()
        self.initial_bb.setBitHot(3) if self.color==0  else self.initial_bb.setBitHot(59) 
        self.position_bb=self.initial_bb
        self.Letter= "Q"  if self.color==0 else "q" 
        self.symbol= "♕" if self.color==0 else "♛"
        self.value=0
        self.tactical_value=0 
        self.table_list=None


class King(): 
    def __init__(self,color :int):
        self.color=color             #{0:"W",1:"B"}
        self.initial_bb=bitboard()
        self.position_bb=bitboard()
        self.motion_bb=bitboard()
        self.attack_bb=bitboard()
        self.castling_rights=[1,1]   # 1:True on Queen side 1:True on King side
        self.Check=False
        self.CheckMate=False
        self.initial_bb.setBitHot(4) if self.color==0  else self.initial_bb.setBitHot(60) 
        self.position_bb=self.initial_bb
        self.Letter= "K"  if self.color==0 else "k" 
        self.symbol= "♔" if self.color==0 else "♚"
        self.value=0
        self.tactical_value=0
        self.table_list=None
