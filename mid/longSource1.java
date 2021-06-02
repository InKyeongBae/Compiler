class Simplesort {
 int[] sort(int numOfelements) {
   String subject = "simple sort";
   int numberOfkeys = 3;
   if (numOfelements == numberOfkeys){
     subject = "sort start";
   }
   int[] key={2,1,3};
   int[] ascend;
   int[] descend;
   int i=0;

   ascend = key;
   while(numberOfkeys != 0){
     int j = i + 1;
     while(numberOfkeys > j){
       if(ascend[i]<=ascend[j]){
         j = numberOfkeys;
       }else{
         int temp = ascend[j];
         ascend[j]=ascend[i];
         ascend[i]=temp;
       }
       j = j + 1;
     }
     i = i + 1;
   }

   descend = ascend;
   while(numberOfkeys != 0){
     int j = i + 1;
     while(j < numberOfkeys ){
       if(descend[i] >= descend[j]){
         j = numberOfkeys;
       }else{
         int temp = descend[j];
         descend[j]=descend[i];
         descend[i]=temp;
       }
       j = j + 1;
     }
     i = i + 1;
   }

   return key;
 }
}
