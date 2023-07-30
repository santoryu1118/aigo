-- https://school.programmers.co.kr/learn/courses/30/lessons/151141?language=mysql#

-- 코드를 입력하세요
with aa as
(
    SELECT * from CAR_RENTAL_COMPANY_CAR where car_type = '트럭'
)

, bb as
(
    select
        aa.car_id,
        aa.car_type,
        aa.daily_fee,
        b.history_id,
        b.start_date,
        b.end_date,
        datediff(b.end_date, b.start_date) + 1 as duration_days,
        case
            when datediff(b.end_date, b.start_date) + 1 >= 90 then '90일 이상'
            when datediff(b.end_date, b.start_date) + 1 >= 30 then '30일 이상'
            when datediff(b.end_date, b.start_date) + 1 >= 7 then '7일 이상'
            else '미달'
        end as duration_name
    from aa
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
        on aa.car_id = b.CAR_ID
)

select
    bb.history_id as HISTORY_ID,
    # bb.duration_days,
    # bb.daily_fee,
    # ifnull(c.discount_rate, 0),
    floor(bb.duration_days * bb.daily_fee * (1- ifnull(c.discount_rate, 0)/100)) as FEE
from bb
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN c
        on bb.car_type = c.car_type
        and bb.duration_name = c.DURATION_TYPE
order by FEE desc, HISTORY_ID desc