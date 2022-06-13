object TD2EX3 extends App{
  def multiple(x:Int)={
    (y:Int)=>{x*y}
  }
  print(multiple(3)(10))
  val triple=multiple(5)
  println( triple(3))

}
