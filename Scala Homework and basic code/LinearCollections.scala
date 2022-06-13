object LinearCollections extends App{

  //Notes de cours

  // Sequence ------------------------------------------------------------------------
  val asequence = Seq(4,2,3,1)

  //indexer un element
  val elem3 = asequence(2); println("elem3 "+ elem3)
  val elem3_ = asequence.apply(2)

  // map/flatmap/filter/foreach
  val incremetedSeq = asequence.map(_ + 1); println("incrementedSeq = "+ incremetedSeq) // [5,3,4,2]
  val flatMappedSeq = asequence.flatMap(x => Seq(x, x+1)); println("flatMappedSeq = "+ flatMappedSeq) // [4,5,2,3,3,4,1,2]
  val filteredSeq = asequence.filter(x => x%2 == 0); println("filteredSeq ="+ filteredSeq) // [4,2]
  asequence.foreach(println)

  //Autres fonctions
  val reversed = asequence.reverse; println(reversed)
  val concatenation = asequence ++ Seq(5,6,7)
  val sorted = asequence.sorted
  val sum = asequence.fold(0)(_+_); println(sum) // sum = 10






  //List  : meme API que Sequence ----------------------------------------------------
  val aList = List(1,2,3)
  val premier = aList.head ; println("premier = "+ premier)
  val reste = aList.tail ; println("reste = "+ reste)
  //appending / prepending
  val appList = 0 +: aList :+ 4
  val prepList = 0 :: aList
  //utility function
  val fillList = List.fill(5)("scala")

  //Ranges  : meme API que Sequence ----------------------------------------------------
  val aRange = 1 to 5 //inclusif
  (1 to 5).foreach(_ => print("Hello ")) ; println

  val aRangeExc = 1 until 5 // 5 non inclus

  //Arrays : are not sequences ----------------------------------------------------------
  val anArray = Array(1,2,3,4,5)

  val arrSeq = anArray.toIndexedSeq // convertir un array to a Sequence
  // les arrays sont mutables
  anArray.update(2,6); anArray.foreach(println)

  //Vectors : des sequences tres rapide dans le cas de donnees volumineuses --------------
  val aVector = Vector(1,2,3,4,5,6)
  //meme API que les sequences sauf que plus rapide

  val vec = for(i <- 1 to 5) yield i
  println(vec)





  // Exercice 1
  println("--------- Exercice 1 -----------")
  val v1 = for (i <- 0L to 9L; j = i * 2 + 1) yield j
  println(v1)

  val v2 = 0L to 20L filter (_ % 2 == 1) // (0 to 20).filter()
  println(v2)

  val v3 = 0L to 9L map (_ * 2 + 1)
  println(v3)

  // Exercice 2
  println("--------- Exercice 2 -----------")
  def diviseurs(x: Int) = { 2 to (x-1) filter (x % _ == 0) }

  /*
  Nous pourrions utiliser +map+ pour faire correspondre chaque élément de la liste
  à une nouvelle liste de facteurs, puis +flatten+ la liste de listes en une seule liste.
  Ou simplement utiliser +flatMap+ une seule fois.
  */

  def uniqueDiviseurs(l: Seq[Int]) = l.flatMap(diviseurs(_))
  //ou bien
  //def uniqueDiviseurs(l: Seq[Int]) = l flatMap diviseurs


  val ld = uniqueDiviseurs(List(9, 11, 13, 15))
  println(ld)

  // Exercice 3
  println("--------- Exercice 3 -----------")
  //-------------------------- Utilisation d'une opération de liste intégrée
  val chars = ('a' to 'f').toList
  def first_take[A](items: List[A], count: Int): List[A] = items take count
  println(first_take(chars, 3))

  //-------------------------- Utilisation d'un for-loop
  def first_for[A](items: List[A], count: Int): List[A] = {
       val l = for (i <- 0 until count) yield items(i)
       l.toList
     }
  println(first_for(chars, 3))
  //Cela fonctionne, mais les performances vont être terribles avec les longues collections non indexées telles que les listes chaînées.

  //-------------------------- Utilisation de foldtLeft
  def first_fold[A](items: List[A], count: Int): List[A] = {
       items.foldLeft[List[A]](Nil) { (a: List[A], i: A) =>
           if (a.size >= count) a else i :: a
         }.reverse
     }
  println(first_fold(chars, 3))

  //-------------------------- Recursive
  def first_recursive[A](items: List[A], count: Int): List[A] = {
       if (count > 0 && items.tail != Nil) items.head :: first_recursive(items.tail, count - 1)
       else Nil
     }
  println(first_recursive(chars, 3))


  // Exercice 4
  println("--------- Exercice 4 -----------")
  val names = List("Harry", "Hermione", "Ron", "Snape")

  //-------------------------- Utilisation de la fonction sortBy
  def longest_sort(l: List[String]): String = l.sortBy(0 - _.size).head
  println(longest_sort(names))

  //-------------------------- Utilisation de la fonction fold
  def longest_fold(l: List[String]): String = {
       l.fold("")((a,i) => if (a.size < i.size) i else a)
     }
  println(longest_fold(names))

  //-------------------------- Utilisation de la fonction reduce
  def longest_reduce(l: List[String]): String = {
       names.reduce((a,i) => if (a.size < i.size) i else a)
     }
  println(longest_reduce(names))


  // Exercice 5
  println("--------- Exercice 5 -----------")
  def reverse[A](src: List[A], dest: List[A] = Nil): List[A] = {
       if (src == Nil) dest else reverse(src.tail, src.head :: dest)
     }
  println(reverse(names))
}
