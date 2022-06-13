object TD2EX4 extends App{
  def fzero(x: String, f: String => Unit): String = { f(x); x }
  println(fzero("hello",(x)=>println(x.length)))
}
