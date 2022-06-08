import numpy as np
from numpy.lib.function_base import copy
from bitboards import bitboard
from Piece import King,Pawn,Rook,Queen,Bishop,Knight
import copy
class Position:
     def __init__(self):  #deals with current position instance
        self.val=""
        self.color={0:"w" ,1:"b" }
        self.tomove=self.color[0]
        #####################
        #####filling Board###
        #####################
        
        self.L0=list()
        s0=Rook(0),Knight(0),Bishop(0),Queen(0),King(0),Pawn(0) #,File.A),Pawn(0,File.B),Pawn(0,File.C),Pawn(0,File.D),Pawn(0,File.E),Pawn(0,File.F),Pawn(0,File.G),Pawn(0,File.H)
        self.L0.extend(s0)
        self.L1=list()
        s1=Rook(1),Knight(1),Bishop(1),Queen(1),King(1),Pawn(1) #,File.A),Pawn(1,File.B),Pawn(1,File.C),Pawn(1,File.D),Pawn(1,File.E),Pawn(1,File.F),Pawn(1,File.G),Pawn(1,File.H)
        self.L1.extend(s1)
        self.D=dict()
        self.D["W"] = self.L0
        self.D["B"] = self.L1
        self.Pieces=list()
        self.Pieces.extend(s0)
        self.Pieces.extend(s1)

        self.BB=bitboard()
        for lis in self.Pieces: 
            self.BB.value |=lis.initial_bb.value
        
        self.fullBoard=bitboard()
        for lis in self.Pieces: 
            self.fullBoard |=lis.position_bb.value

     def get_b_string(self,a,length=64):
        a=np.uint64(a)
        ch=bin(a)
        ch=ch[2:].zfill(length)[::-1] 
        print(ch)
        return ch
     def get_Piece_by_sq(self ,sq: int):
        for i in self.Pieces:       #i is piece
            if (i.position_bb.value == np.uint64(sq)):
                break
        return i
     def generate_FEN(self):  #A FEN is a string that represents the state of a position and 
         self.fen=''          #from which we can reconstruct the history of the game so far
         ch=self.get_b_string(self.BB)
         for i in range(64):
             if ch[i]==1:
                 self.fen+=self.get_Piece_by_sq(i).Letter
             if i%8==0:
                 self.fen+="/"
         self.fen+=' '+self.tomove # +color of who to move next . w means white moves next
         if (self.L0[4].castling_rights[1]==self.L0[3].castling_rights[0]==self.L1[4].castling_rights[1]==self.L1[3].castling_rights[0]==0):
             self.fen+="-"
         else:
            if self.L0[4].castling_rights[1]==1:
                self.fen+=self.L0[4].Letter
            if self.L0[3].castling_rights[0]==1:
                self.fen+=self.L0[3].Letter
            if self.L1[4].castling_rights[1]==1:
                self.fen+=self.L1[4].Letter
            if self.L1[3].castling_rights[0]==1:
                self.fen+=self.L1[3].Letter
         #TO DO
         #en passant algebric target square (square of pawn who just moved 2 squares) else takes "-"
         #Halfmove clock: The number of ply-s since the last capture or pawn advance
         #Fullmove number:number of full move.starts at 1,incremented after Black's move

         #write FEN to txt file
     def create_position_from_FEN(ch):
         pass
     def get_move_list(self):
         List_move_W=[]
         List_move_B=[]
         for Piece in self.D["W"]:
             for i in range(64):
                M=Move()
                q=M.move(Piece,Piece.position_bb.get_squares_from_bb(),i,1)
                List_move_W.append(q)
        for Piece in self.D["W"]:
             for i in range(64):
                M=Move()
                q=M.move(Piece,Piece.position_bb.get_squares_from_bb(),i,1)
                List_move_W.append(q)
        return List_move_W,List_move_B

class File:
    A = set( [np.uint64(i) for i in range(0,64,8)]) 
    B = set( [np.uint64(i) for i in range(1,64,8)])
    C = set( [np.uint64(i) for i in range(2,64,8)])
    D = set( [np.uint64(i) for i in range(3,64,8)])
    E = set( [np.uint64(i) for i in range(4,64,8)])
    F = set( [np.uint64(i) for i in range(5,64,8)])
    G = set( [np.uint64(i) for i in range(6,64,8)])
    H = set( [np.uint64(i) for i in range(7,64,8)])

    files = [A, B, C, D, E, F, G, H]

class Rank:
    x1 = set( [np.uint64(i) for i in range(0,8)])
    x2 = set( [np.uint64(i) for i in range(8,16)])
    x3 = set( [np.uint64(i) for i in range(16,24)])
    x4 = set( [np.uint64(i) for i in range(24,32)])
    x5 = set( [np.uint64(i) for i in range(32,40)])
    x6 = set( [np.uint64(i) for i in range(40,48)])
    x7 = set( [np.uint64(i) for i in range(48,56)])
    x8 = set( [np.uint64(i) for i in range(56,64)])

    ranks = [x1, x2, x3, x4, x5, x6, x7, x8]
#Notice:
""" northwest    north   northeast
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast"""
"""  also  for square [i th rank ,j th file] 
we can find diag i,j = square[i+1,j]+square[i,j+1]-square[i,j]
piece on square 10 , the northwestern diag is 9+18-10=17 
so deducing diag class from rank file is possible but we will hard code cuz bytes of storage< computation time  """
class Diag:
   
    Dw8 = set ([np.uint64(56)])
    Dw7 = set ([np.uint64(i) for i in range(40,59,9)])
    Dw6 = set ([np.uint64(i) for i in range(24,61,9)])
    Dw5 = set ([np.uint64(i) for i in range(8,63,9)])
    Dw4 = set ([np.uint64(i) for i in range(1,56,9)])
    Dw3 = set ([np.uint64(i) for i in range(3,40,9)])
    Dw2 = set ([np.uint64(i) for i in range(5,24,9)])
    Dw1 = set ([np.uint64(7)])
    #### now for black diagonals
    Db1 = set ([np.uint64(i) for i in range(0,64,9)])
    Db2 = set ([np.uint64(i) for i in range(2,48,9)])
    Db3 = set ([np.uint64(i) for i in range(4,32,9)])
    Db4 = set ([np.uint64(i) for i in range(6,16,9)])
    Db5 = set ([np.uint64(i) for i in range(16,62,9)])
    Db6 = set ([np.uint64(i) for i in range(32,60,9)])
    Db7 = set ([np.uint64(i) for i in range(48,58,9)])
    White_squares= Dw1 |Dw2 |Dw3 |Dw4 |Dw5 |Dw6 |Dw7|Dw8
    Black_squares=Db1 | Db2 | Db3 |Db4 |Db5 |Db6 |Db7 
    DW= [ Dw1 ,Dw2 ,Dw3 ,Dw4 ,Dw5 ,Dw6 ,Dw7,Dw8]
    DB= [Db1 , Db2 , Db3 ,Db4 ,Db5 ,Db6 ,Db7]    
class antiDiag:

    Db8 = set ([np.uint64(0)])
    Db9 = set ([np.uint64(i) for i in range(2,17,7)])
    Db10 = set ([np.uint64(i) for i in range(4,33,7)])
    Db11 = set ([np.uint64(i) for i in range(6,49,7)])
    Db12 = set ([np.uint64(i) for i in range(15,58,7)])
    Db13 = set ([np.uint64(i) for i in range(31,60,7)])
    Db14 = set ([np.uint64(i) for i in range(47,62,7)])
    Db15 = set ([np.uint64(63)])

    Dw15 = set ([np.uint64(i) for i in range(55,63,7)])
    Dw14 = set ([np.uint64(i) for i in range(39,61,7)])
    Dw13 = set ([np.uint64(i) for i in range(23,59,7)])
    Dw12 = set ([np.uint64(i) for i in range(1,9,7)])
    Dw11 = set ([np.uint64(i) for i in range(3,25,7)])
    Dw10 = set ([np.uint64(i) for i in range(5,41,7)])
    Dw9 = set ([np.uint64(i) for i in range(7,57,7)])   
    Dw8 = set ([np.uint64(56)])

    White_squares= Dw8 |Dw9 |Dw10 |Dw11 |Dw12|Dw13 |Dw14 |Db15
    Black_squares=Db8 | Db9 | Db10 |Db11 |Db12 |Db13 |Db14|Db15
    DW= [ Dw8 ,Dw9 ,Dw10 ,Dw11 ,Dw12,Dw13 ,Dw14 ,Db15]
    DB= [Db8 , Db9 , Db10 ,Db11 ,Db12 ,Db13 ,Db14,Db15]

class Move:
        #def make_move(sq_fr:int ,sq_to :int):
        #check pseudo-legality
        #check check
        #update bitboard
        #update attackers
   #def unmake_move() 


    def __init__(self,Pos:Position):
        self.cur_pos=Pos
        pass
        """
        ********
        takes position bitboard
        from to
        checks for pseudo legality:
            1set bit hot , 2clear bit , (3)clear bit of attacked piece
        change who to move

        *******move representation function
        generate  code for move with"x"
        prints new board
        types:
        capture
        motion
        pseudo legality
        legality
        """
        #return True if move is made , False if not
    def move(self,P,f_sq,t_sq,c=0):  #c is 1 if the move is a castle and we have to flag it to the FEN and game history
        Check=False
        Capture=False
        Castle_pin=False
        color=P.color
        try:
        assert (f_sq == P.position_bb.get_squares_from_bb()) #TO DO : remove the pieces on the first intersection and beyond(ally+enemy)
        b= self.cur_pos.fullBoard
        for x in (b.value & P.motion_bb.value):
            sq=P.motion_bb.bitscan_forward(b.value)
            blocked_mv &= ~sq
        allowed_mv.value=P.motion_bb.value - blocked_mv
        for piece in (self.cur_pos.D[abs(1-self.cur_pos.to_move)]):#adding back the enemy pieces (a capture)
            allowed_mv.value|= piece.position_bb.value
        assert (t_sq in allowed_mv.get_squares_from_bb())

        for piece in (self.cur_pos.D[abs(1-self.cur_pos.to_move)]):#does my capture leave my king in check ? am i pinned ?
            if (piece.color!=color) & (piece.position_bb.value== np.uint64(t_sq)):
                Capture=True
            if (K.color==color) & (K.position_bb.value & piece.motion_bb.value !=0):
                Check=True
            if (R.color==color) & (R.position_bb.value & piece.motion_bb.value !=0):    
                Castle_pin=True
        assert Check==False
        
        if Capture ==True :                     #removing the captured piece and the entire object if last of it's kind
            Pr=self.cur_pos.get_Piece_by_sq(t_sq)#add me if there's a promotion but until then this speeds up comparisons
            Pr.position_bb.clearBit(t_sq)
            if Pr.position_bb==0:
                for piece in (self.cur_pos.D[abs(1-self.cur_pos.to_move)]): 
                    if piece.color==Pr.color & type(piece)==type(Pr)
                      Pr=piece
                      self.cur_pos.Pieces.remove(piece)
            self.cur_pos.fullBoard.value=self.cur_pos.fullBoard.value -Pr.position_bb.value #remove enemy piece
        self.cur_pos.fullBoard.value=self.cur_pos.fullBoard.value & ~P.position_bb.value    #change my piece's position Part I
        P.position_bb.clearBit(f_sq)
        P.Position_bb.setHotBit(t_sq) #change my piece's position Part II
        self.cur_pos.fullBoard.value=self.cur_pos.fullBoard.value|P.position_bb.value #update the board after removal 

        assert Catle_pin ==False
        if c=1 :  #updating castling right for king and rook of this rook
        for piece in self.curPos.Pieces :
            if type(piece)==King :                       
                if (piece.color==color) and (t_sq in File.A |File.B |File.C |File.D): #queen side castle
                    piece.castling_rights=[0]=0
                    piece.position_bb.clearBit(f_sq)
                    piece.Position_bb.setHotBit(t_sq)
            if type(piece)==Rook :
                if (piece.color==color) and (t_sq in File.A |File.B |File.C |File.D):
                    piece.castling_rights=[0]=0
                    piece.position_bb.clearBit(piece.position_bb.get_squares_from_bb()[0])
                    piece.Position_bb.setHotBit(t_sq+1)
            if type(piece)==King :                       
                if (piece.color==color) and (t_sq in File.E |File.F |File.G |File.H): #King side castle
                    piece.castling_rights=[1]=0
                    piece.position_bb.clearBit(f_sq)
                    piece.Position_bb.setHotBit(t_sq)
            if type(piece)==Rook :
                if (piece.color==color) and (t_sq in File.E |File.F |File.G |File.H):
                    piece.castling_rights[1]=0
                    piece.position_bb.clearBit(piece.position_bb.get_squares_from_bb()[1])
                    piece.Position_bb.setHotBit(t_sq-1)
         #FEN variable needs to change to reflect the castling
         for i in self.cur_pos.color.keys()
            if i != self.tomove:
                self.tomove=self.cur_pos.color[i]
        except AssertionError:
            print 'illegal move , try again'
            raise
            return None,False
        l=list()
        l.append(P)
        l.append(f_sq)
        l.append(t_sq)
        return l ,True

    def Piece_coord(self,P): #return rank anf file of a piece P
        ch=self.cur_pos.get_b_string(P.position_bb,length=64)
        D=dict()
        for i,c in enumerate(ch):
            if c=="1":
                for R in Rank.ranks :
                    if i in R:
                        break 
                for F in File.files:
                    if i in F :  
                        break
                D[i]=(R,F)
        return D
    
    def Piece_Diag_coord(self,P): #return Diagonals of a piece P
        ch=self.cur_pos.get_b_string(P.position_bb,length=64)
        D=dict()
        for i,c in enumerate(ch):
            if i in Diag.White_squares:
                if c=="1":
                    for Dn in Diag.DW :
                        if i in Dn:
                            break 
                    for aDn in antiDiag.DW:
                        if i in aDn :  
                            break
                    D[i]=(Dn,aDn)
            if i in Diag.Black_squares:
                if c=="1":
                    for Dn in Diag.DB :
                        if i in Dn:
                            break 
                    for aDn in antiDiag.DB:
                        if i in aDn :  
                            break
                    D[i]=(Dn,aDn)
        return D
    
    def king_move(self,P):
        assert isinstance(P, King)
        b=bitboard()
        i=P.position_bb.get_squares_from_bb()[0]
        if ((i in (File.B| File.C|File.D|File.E|File.F|File.G)) and (i in (Rank.x2|Rank.x3|Rank.x4|Rank.x5|Rank.x6|Rank.x7) )):
            b.value |= np.uint64(1)<<np.uint64(i+1)
            b.value |= np.uint64(1)<<np.uint64(i-1)
            b.value |= np.uint64(1)<<np.uint64(i+9)
            b.value |= np.uint64(1)<<np.uint64(i-9)
            b.value |= np.uint64(1)<<np.uint64(i+8)
            b.value |= np.uint64(1)<<np.uint64(i-8)
            b.value |= np.uint64(1)<<np.uint64(i+7)
            b.value |= np.uint64(1)<<np.uint64(i-7)
        elif ((i in File.A) and (i not in (Rank.x1|Rank.x8))) :
            b.value |= np.uint64(1)<<np.uint64(i+1)
            b.value |= np.uint64(1)<<np.uint64(i+9)
            b.value |= np.uint64(1)<<np.uint64(i+8)
            b.value |= np.uint64(1)<<np.uint64(i-8)
            b.value |= np.uint64(1)<<np.uint64(i-7)
        elif i in File.H and (i not in (Rank.x1|Rank.x8)) :
            b.value |= np.uint64(1)<<np.uint64(i-1)
            b.value |= np.uint64(1)<<np.uint64(i-9)
            b.value |= np.uint64(1)<<np.uint64(i+8)
            b.value |= np.uint64(1)<<np.uint64(i-8)
            b.value |= np.uint64(1)<<np.uint64(i+7)
        elif i not in File.A|File.H   and i in Rank.x1:
            b.value |= np.uint64(1)<<np.uint64(i+1)
            b.value |= np.uint64(1)<<np.uint64(i-1)
            b.value |= np.uint64(1)<<np.uint64(i+9)
            b.value |= np.uint64(1)<<np.uint64(i+8)
            b.value |= np.uint64(1)<<np.uint64(i+7)
        elif i not in File.A|File.H   and i in Rank.x8:
            b.value |= np.uint64(1)<<np.uint64(i+1)
            b.value |= np.uint64(1)<<np.uint64(i-1)
            b.value |= np.uint64(1)<<np.uint64(i-9)
            b.value |= np.uint64(1)<<np.uint64(i-8)
            b.value |= np.uint64(1)<<np.uint64(i-7)
        elif i == 0:
            b.value |= np.uint64(1)<<np.uint64(i+8)
            b.value |= np.uint64(1)<<np.uint64(i+9)
            b.value |= np.uint64(1)<<np.uint64(i+1)
        elif i == 56:
            b.value |= np.uint64(1)<<np.uint64(i-8)
            b.value |= np.uint64(1)<<np.uint64(i-7)
            b.value |= np.uint64(1)<<np.uint64(i+1)
        elif i == 63:
            b.value |= np.uint64(1)<<np.uint64(i-8)
            b.value |= np.uint64(1)<<np.uint64(i-9)
            b.value |= np.uint64(1)<<np.uint64(i-1)
        elif i==7 :
            b.value |= np.uint64(1)<<np.uint64(i+8)
            b.value |= np.uint64(1)<<np.uint64(i+7)
            b.value |= np.uint64(1)<<np.uint64(i-1)
        """for line in D.values():
            for i in line[0]: #R is a list
                if i in D.keys():
                    continue
                else:
                    b.value |= np.uint64(1)<<np.uint64(1)
            for i in line[1]: #F is a list
                if i in D.keys():
                    continue
                else:
                    b.value |= np.uint64(1)<<np.uint64(1)
            #self.cur_pos.get_b_string(b)"""
        return b
    def hv_sliding(self,P):
        assert isinstance(P, Rook) or isinstance(P, Queen)
        D=self.Piece_coord(P)
        b=bitboard()
        for line in D.values():
            for i in line[0]: #R is a list
                if i in D.keys():
                    continue
                else:
                    b.value |= np.uint64(1)<<np.uint64(i)
            for i in line[1]: #F is a list
                if i in D.keys():
                    continue
                else:
                    b.value |= np.uint64(1)<<np.uint64(i)
            #self.cur_pos.get_b_string(b)
        return b
    def pawn_move(self,P):
        assert isinstance(P, Pawn)
        D=self.Piece_coord(P)
        b=bitboard()
        if P.color==0:
            for index in D.keys() :
                if index in Rank.x2:
                    b.value |= np.uint64(1)<<np.uint64(index+8)
                    b.value |= np.uint64(1)<<np.uint64(index+16)
                else:
                    b.value |= np.uint64(1)<<np.uint64(index+8)
        elif P.color==1:
            for index in D.keys() :
                if index in Rank.x7:
                    b.value |= np.uint64(1)<<np.uint64(index-8)
                    b.value |= np.uint64(1)<<np.uint64(index-16)
                else :
                    b.value |= np.uint64(1)<<np.uint64(index-8)
                #self.cur_pos.get_b_string(b)
        return b
    def Knight_move(self,P):
        assert isinstance(P, Knight)
        D=self.Piece_coord(P)
        b=bitboard()
        L=set([-17,-10,6,15,17,10,-6,-15])
        L0=set([15,17]) #North long move
        L1=set([-15,-17])#South long move
        L2=set([6,-10]) #West long move
        L3=set([-6,10]) #Eeast long move
        ######center box
        for i in D.keys():
            if ((i in (File.C|File.D|File.E|File.F)) and (i in (Rank.x3|Rank.x4|Rank.x5|Rank.x6 ))):
                b.value |= np.uint64(1)<<np.uint64(i+15)
                b.value |= np.uint64(1)<<np.uint64(i-15)
                b.value |= np.uint64(1)<<np.uint64(i+17)
                b.value |= np.uint64(1)<<np.uint64(i-17)
                b.value |= np.uint64(1)<<np.uint64(i+6)
                b.value |= np.uint64(1)<<np.uint64(i-6)
                b.value |= np.uint64(1)<<np.uint64(i+10)
                b.value |= np.uint64(1)<<np.uint64(i-10)
        #######middle box
            elif i in range(10,14):
                for j in L-L1:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i in range(50,54):
                for j in L-L0:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i in range(17,42,8):
                for j in L-L2:
                    b.value |= np.uint64(1)<<np.uint64(i+j)                
            elif i in range(22,47,8):
                for j in L-L3:
                    b.value |= np.uint64(1)<<np.uint64(i+j) 
            elif i==9:
                for j in L-(L1|L2):
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==14:
                for j in L-(L1|L3):
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==54:
                for j in L-(L0|L3):
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==49:
                for j in L-(L0|L2):
                    b.value |= np.uint64(1)<<np.uint64(i+j)
        #########outer box:
            elif ((i in File.A) and (i in (Rank.x3|Rank.x4|Rank.x5|Rank.x6))) :
                for j in [-6,10,17,-15]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i in File.H and (i in (Rank.x3|Rank.x4|Rank.x5|Rank.x6)) :
                for j in [6,-10,15,-17]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i in File.C|File.D|File.E|File.F   and i in Rank.x1:
                for j in [15,17,10,6]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i in File.C|File.D|File.E|File.F   and i in Rank.x8:
                for j in [-15,-17,-10,-6]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==1:
                for j in [15,17,10]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==8:
                for j in [-6,10,17]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==48:
                for j in [-6,10,-15]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==57:
                for j in [-17,-15,-6]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==62:
                for j in [-10,-15,-17]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==55:
                for j in [6,-10,-17]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==15:
                for j in [15,6,-10]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==6:
                for j in [6,15,17]:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i == 0:
                for j in 10,17:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i == 56:
                for j in -15,-6:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i == 63:
                for j in -10,-17:
                    b.value |= np.uint64(1)<<np.uint64(i+j)
            elif i==7 :
                for j in 15,6 :
                    b.value |= np.uint64(1)<<np.uint64(i+j)
        return b
    def Diag_sliding(self,P):
        assert isinstance(P, Queen) or  isinstance(P, Bishop)
        D=self.Piece_Diag_coord(P) #square : trigD,antitrigD  
        b=bitboard()
        for line in D.values():
            for i in line[0]: 
                if i in D.keys():
                    continue
                else:
                    b.value |= np.uint64(1)<<np.uint64(i)
            for j in line[1]: 
                if j in D.keys():
                    continue
                else:
                    b.value |= np.uint64(1)<<np.uint64(j)
            #self.cur_pos.get_b_string(b)
        return b
    def Queen_move(self, P):
        assert isinstance(P, Queen)
        b=bitboard()
        b.value=self.Diag_sliding(P).value|self.hv_sliding(P).value
        return b

