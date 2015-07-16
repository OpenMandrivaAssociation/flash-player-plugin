
version=`grep ^Version flash-player-plugin.spec | awk '{print $2}'`

for urlandno in $(grep "^\%define downurl" flash-player-plugin.spec | grep -v \%nil | awk '{print substr($2,length($2),1) "|" $3}')
do
   
   IFS="|" read -a myarray <<< "$urlandno"

   url=${myarray[1]}
   no=${myarray[0]}

   fin=`echo $url | sed -e "s/%{version}/$version/g"`

   file=`basename $fin`

   wget $fin
   sum=`sha256sum $file | awk '{print $1}'`

   fsize=`stat --printf="%s" $file`

   echo $fsize
   #define tsha256sum1     a4b229470e62fedcd7edbf5cdf2bb90f8f43f1a6fa5286240e35433d7c73a125:6918554

   sed -i "s/ tsha256sum${no}.*/ tsha256sum${no}\t$sum:$fsize/" flash-player-plugin.spec
   rm -f $file
done
