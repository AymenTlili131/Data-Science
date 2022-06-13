object TestCollections  extends  App {
  val s = Seq(4, 2, 3, 1)
  var elem = s(2);
  println("elem3=" + elem)
  var elem2 = s.apply(2)
  println("elem3=" + elem)
  val incrementedSeq = s.map(_ + 1);
  println("incremented Sequence=" + incrementedSeq)
  val flatmapSeq = s.flatMap(x => Seq(x, x + 1));
  println("flat map Sequence=" + flatmapSeq);
  val filterSeq=s.filter(x=>x%2==0);
  println("filter Sequence=" + filterSeq);
  s.foreach(println)
  val reserved=s.reverse;
  println("reversed Sequence=" + reserved);
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
  val concatenation = asequence ++ Seq(5,6,7)//concatination
  val sorted = asequence.sorted//trier la list par ordre croissant
  val sum = asequence.fold(0)(_+_); println(sum) // sum = 10    0:la valeur de somme commnce par 0  //_+_ fonction pour faire le somme






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



  val vec=for(i<- 1 to 5) yield i //injecter les valeurs dans un tampon puis les recupérer dans le vector
  //Vectors : des sequences tres rapide dans le cas de donnees volumineuses --------------
  val aVector = Vector(1,2,3,4,5,6)
  //meme API que les sequences sauf que plus rapide


}


