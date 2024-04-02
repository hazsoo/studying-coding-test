-- 코드를 입력하세요
SELECT A.REST_ID
    , A.REST_NAME
    , A.FOOD_TYPE
    , A.FAVORITES
    , A.ADDRESS
    , ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS A
LEFT JOIN REST_REVIEW AS B ON A.REST_ID = B.REST_ID
WHERE ADDRESS LIKE '서울%'
AND REVIEW_SCORE IS NOT NULL
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC