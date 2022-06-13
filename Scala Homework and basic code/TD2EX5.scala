object TD2EX5 extends App{
  val tab= Array[Int](1,2,3,-3,5,-9)
  println(tab.min)
  tab.sorted.foreach(println)
  /*tab.reverse.foreach(print)
  tab.foreach(print)
  tab.foreach(x=>{
    if(x>0) println(x)
  })*/
  /*def affiche(tab:Array[Int],f:Int=>Boolean)={
    tab.filter(f).foreach(println)
  }
  affiche(tab,x=>x> -100)
*/
  /*tab.foreach(println)

  tab.foreach(println _)

  tab.foreach(x=>{
    if(x>0) println(x)
  })
  tab.filter(_>0).foreach(println)
  tab.filter(x=>x>0).foreach(println)*/
}
