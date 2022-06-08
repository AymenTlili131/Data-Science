import Position_op
#q_learning in gridworld.py
#q_learning.py with epochs and similer  Gym API
class Agent : 
    #list of piece
    #list of moves 
       #compare thsi to Perft 12 , if false check the move generation function and debug it
    def __init__(self,a:int):
         Score=0
         assert a in {0,1}
         self.color=a
         self.piece_List=[]
         self.moves_List=[]
         self.Position=Position()
    #transposition table
        #FEN to evaluation dict . size = top 10^^8
    #hash function 

    #killer move heuristic
    #move ordering 
        #Capture Yes ?
        #killer moves 3 slots
        #null move pruning
        #king safety increase

    #shallow pruning 

    #Negamax
    def NegaMax(pos, depth, alpha, beta): if depth = 0:
        return evaluate(pos) bestSoFar = -infinityfor move in pos.legal_moves:
        # Note the order of -beta and -alpha
        value = -NegaMax(after_move(pos, move), depth - 1, -beta, -alpha) 
        if value > bestSoFar: # update bestSoFar
         bestSoFar = valueif bestSoFar > beta: # pruning condition
         return bestSoFaralpha = max(alpha, bestSoFar)
        return bestSoFaralpha = max(alpha, bestSoFar)

    #Eval function:
    #distance king distance to attacked squares 
    #number of legal moves 
        #capture moves are more valuable
        #Quiesence search
    
    #Q learning on episode end
        #approximate Q to function instead of tabular method 
        #Semi gradient target calculation
        #stochastic grad descent

    #link to EGBT when # of pieces <= 5  
    #http://oics.olympuschess.com/tracker/index.php?page_number=&
    #download 
    #checksum
    #execute with MKAT tool
    #extract to text file
    #order by evaluation
    #parse from text file 
 
