object TD2EX1 extends App{
  val f = (a:Int,b:Int)=>{
    //if(a>b) a else b
    (a>b) match {
      case true => a
      case false => b
    }

  }
  def max(a:Int,b:Int,c:Int,f:(Int,Int)=>Int): Int ={
    f(f(a,b),c)
  }
  println(max(1,2,3,f))
}
