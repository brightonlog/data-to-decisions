-- 00_long.sql : 와이드(카테고리=컬럼) → 롱(date, sector, idx) 변환. 이후 모든 쿼리의 기초.
-- total 컬럼은 UNPIVOT 대상에서 제외 → 각 행에 그대로 붙음 (비중 계산용).
CREATE OR REPLACE VIEW v_monthly_long AS
UNPIVOT monthly_sector_sa
ON entertainment, groceries, health, restaurants, services,
   shopping, transport, travel, utilities
INTO NAME sector VALUE idx;
