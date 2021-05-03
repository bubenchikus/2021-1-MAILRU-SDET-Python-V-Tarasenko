> result.txt ; OUT=$(grep -c ' *.*.*.* ' access.log); printf "\nобщее количество запросов:  \n%s\n" "$OUT" >> result.txt;

for PARAM in 'GET' 'POST' 'HEAD' 'PUT' ; do
  OUT=$(grep -c $PARAM access.log); printf "\nколичество %s-запросов: \n%s" "$PARAM" "$OUT" >> result.txt
done

OUT=$(awk -F ' ' '{print $7}' access.log | sort | uniq -c | sort -nr| head -10); printf "\n\nТОП- 10 самых частых запросов:\n%s" "$OUT" >> result.txt

OUT=$(grep -i '" 4[0-9][0-9]' access.log | awk -F ' ' '{print $1,$7,$9,$10}' | uniq | sort -k4 -nr | head -5);
printf "\n\nТОП-5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n%s\n" "$OUT" >> result.txt

OUT=$(grep -i '" 5[0-9][0-9]' access.log | awk -F ' ' '{print $1}' | uniq -c| sort -k1 -nr | head -5);
printf "\n\nТОП-5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n%s\n" "$OUT" >> result.txt







