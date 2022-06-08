from __future__ import division
import numpy as np


class bitboard:
    def __init__ (self):
        self.value=np.uint64(0)
        self.val=''
    def __int__(self):
        return int(self.value)
    def __coerce__(self, other):
        if other is None: other = 0.0
        return (type(other)(self.value), other)
    def __add__(self, other):
        return self.value+other
    def __sub__(self, other):
        return self.value-other
    def __mul__(self, other):
        return self.value*other
    def __floordiv__(self, other):
        return self.value// other
    def __div__(self, other):
        return self.value / other
    def __truediv__(self, other):
        return division(self.value,other) 
    def __mod__(self, other):
        return self.value% other
    def __divmod__(self, other):
        return divmod(self.value,other)
    def __pow__(self,other) :
        return self.value ** other
    def __invert__(self):
        return ~self.value
    def ___rlshift__(self, other):
        return self.value << other
    """Implements reflected left bitwise shift using the << operator."""
    def _rshift__(self, other):
        return self.value >>other
    """Implements reflected right bitwise shift using the >> operator."""
    def __rand__(self, other):
        return self.value & other
    """Implements reflected bitwise and using the & operator."""
    def __ror__(self, other):
        self.value =self.value | other.value
        return self.value
    """Implements reflected bitwise or using the | operator."""
    def __rxor__(self, other):
        return self.value ^ other
    """Implements reflected bitwise xor using the ^ operator."""


    """ converts int a to 64 bit long string """
    def get_bytes_bitboard(self)->str: 
        x=(bin(self.value))[2:].zfill(64)
        return x
    def get_squares_from_bb(self)->list:
        squares=[]
        for i,bit in enumerate(reversed(self.get_bytes_bitboard())):
            if int(bit)!=0 :
                squares.append(i)
        return squares

    def setBitHot(self, bit:int ):
        x=np.uint64(0)
        self.value|=np.uint64( (x | (np.uint64(1) << np.uint64(bit))))
        

    def clearBit(self, bit:int ):
        x=self.get_squares_from_bb()
        assert bit in x
        x.remove(bit)
        b=bitboard()
        for i in x :
            b.setBitHot(i)
        self.value=b.value

 
    def print_bitboard(self,N):    #TO DO :update this to include symbol instead of O
        self.val='' #self.occupied_squares_bitboards
        ch=bin(self.value)[2:].zfill(64)
        for i in range(0,N,int(sqrt(N))):   
            row=ch[i:i+][::-1]
            self.val+='\n'
            for i,c in enumerate(row):
                if c=='0':
                  self.val +='-'
                elif c=='1' :
                    self.val+="O"
                    """
                    P=self.get_Piece_by_sq(i)
                    self.val+=P.symbol
                    else:
                        pass
                    """
        print(self.val)

    def bitscan_forward(bitboard :np.uint64):
        i=1
        while not(bitboard>>np.uint64(i))%2:
            i+=1
        return i

    def bitscan_reverse(self):
        def lookup_most_significant_1_bit(bit):
            if bit> np.uint64(127):
                return np.uint64(7)
            if bit> np.uint64(63):
                return np.uint64(6)
            if bit> np.uint64(31):
                return np.uint64(5)
            if bit >np.uint64(15):
                return np.uint64(4)
            if bit >np.uint64(7):
                return np.uint64(3)
            if bit >np.uint64(1):
                return np.uint64(1)
            return np.uint64(0)
        if not self:
            raise Exception("You don't want to reverse scan an empty bitboard , right ? ")
        result=np.uint64(0)
        if self > 0xFFFFFFFF:
            self>>=np.uint(32)
            result=np.uint(32)
        if self > 0xFFFF:
            self>>=np.uint(16)
            result=np.uint(16)
        if self > 0xFF:
            self>>=np.uint(8)
            result=np.uint(8)
        return result+lookup_most_significant_1_bit(self)
    #bitboards representing the squares attacked by a certain piece on a certain square,