class Voiture private (val fabricant: String, val modele: String) {//private pour interdire de mettre le mot cle new avant l'instantiation
  var vitesse: Double = 0;
  var isOn: Boolean = false;
  def start(): Unit = {
    isOn = true
    println(s"Voiture started ")
  }
  import Voiture._
  def accelerer(rate: Double): Unit = {
    vitesse += rate
    if(rate+vitesse>vitesseMax){
      vitesse=Voiture.vitesseMax
      println(s"Voiture accelere a $vitesse par seconde.")
    }
    else{
      println(s"Voiture accelere a $vitesse par seconde.")

    }
  }
  def decelerer(rate: Double): Unit = {
    vitesse -= rate
    println(s"Voiture ralenti a $vitesse par seconde.")
  }
  def stop(): Unit = {
    vitesse = 0;
    isOn = false;
    println("Voiture s’arrete.")
  }
}
object Voiture{
  val vitesseMax:Double=50
  def apply (fabricant: String,  modele: String)={
    new Voiture(fabricant, modele)
  }
}


object td3ex1 extends App{
  var V:Voiture=  Voiture("Toyota","Rav4")
  V.start()
  V.accelerer(20)
  V.accelerer(40)
  V.decelerer(30)
  V.decelerer(20)
  V.stop()
}
