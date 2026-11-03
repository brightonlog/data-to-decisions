# 공통 컨텍스트 — Revolut S&O 포트폴리오 (모든 세션 공유)

## 0. 목표
Revolut Graduate Programme 2027 Strategy & Operations Manager. 2027.09 intake. 지원 마감 2026.12 전.
비STEM 학위 → 포트폴리오 증거로 대체. LinkedIn으로 현직 S&O 3~5명에게 피드백 요청 후 지원.

## 1. 가치 표현 원칙 (확정)
- **본문(케이스)**: 가치 단어 쓰지 않음. 행동·수치·구조로만 증명.
- **명시는 한 곳**: 사이트 하단 "Fit" 섹션에 5개 가치 ↔ 증거 1:1 표. 각 행 1줄 + 수치. 그게 전부.
- **커버레터/지원서**: 가치 단어 1~2개까지 허용. 반드시 수치 동반.
- **금지어**: 열정, 성실, hardworking, 혁신적, 역량을 발휘, 값진 경험, 최선을 다해. 자기 서술 형용사 전부.

### 케이스 섹션 ↔ 가치 (암묵 매핑, 라벨 안 붙임)
| 케이스 섹션 | 증명하는 가치 |
|---|---|
| 0 Context · 1 Insight · 2 Problem | Think Deeper |
| 3 Solution · 4 Rollout | Get It Done |
| 5 Metrics · 6 Feedback | Never Settle |
| 7 Assumptions | Think Deeper (지적 정직) |
| 1장 요약 + 부록 구조, 디테일 품질 | Deliver WOW |
| 피드백 주고받은 사례 (Case C) | Dream Team |

### Fit 표 (사이트 하단, 현재 초안)
| 가치 | 증거 1줄 |
|---|---|
| Never Settle | Non-STEM → 1,628h SW/AI → top 2% of 2,000 selected as coach |
| Get It Done | Changed official grading process → AI adoption 69% → 93% (+24pp) in one cycle |
| Think Deeper | Diagnosed adoption gap as incentive problem, not awareness; chose evaluation lever over training |
| Deliver WOW | Ops automation for 800 trainees (수치 측정 후 기입) |
| Dream Team | (코칭 피드백 사례 — 정리 후 기입) |

## 2. 모든 사례의 공식
> [1. 데이터 분석]로 병목을 정량화 → [2. 기획]을 세워 타 부서와 협업/협상 → [3. 프로세스 변경]으로 지표 X%p 개선.
세 단계 전부 수치. 하나라도 비면 사례 아님.

## 3. 헤더 한 줄
`Non-STEM → 1,628h SW/AI → top 2% coach → running ops for 800 trainees. Targeting Strategy & Ops.`

## 4. 케이스 템플릿
```
[제목] 문제 한 줄 → 결론 한 줄 (수치)
0 Context · 1 Insight(≤3) · 2 Problem · 3 Solution(2~3안) · 4 Rollout(+첫 48시간 3줄) · 5 Metrics(선행/결과/중단) · 6 Feedback · 7 Assumptions · 부록
```
1장 요약 = 스크롤 1화면. SQL·차트·전문은 부록.

## 5. 케이스 목록
| 케이스 | 데이터 | 상태 |
|---|---|---|
| A. ONS 소비 지수 → 제품 제안 | ONS Revolut debit card (3 에디션 각각) | DuckDB 로드 완료. Q1~Q6 SQL 직접 작성 중 |
| B. 사기 검토 큐 운영 | Revolut take-home 688k | 데이터 확보 필요 |
| C. SSAFY 평가 기준 변경 → AI 사용률 69→93% (실사례, 메인) | 자체 | 측정 방법·기간·루브릭 확인 필요 |
| C'. SSAFY 800명 운영 자동화 (실사례) | 자체 | 전후 수치 측정 필요 |

## 6. 수치 표기 규칙
- 변화는 %p로. "69% → 93% (+24pp)". "93% 개선" 금지.
- 측정 방법·표본 명시. 없으면 쓰지 않음.
- 인과 주장 시 대안 요인 한 줄 인정.
- 내 역할 범위 솔직히. 결정권자 명시.

## 7. 문체 (영문)
- 단문. 결론 먼저. 수치 먼저.
- 능동태. 주어 = I 또는 구체 대상.
- 한 섹션 ≤ 5줄.

## 8. 스택·구조
| 층 | 도구 |
|---|---|
| 분석 | DuckDB → BigQuery Sandbox(대규모) |
| 서빙 | Neon Postgres |
| 사이트 | Next.js + MDX + Tailwind on Vercel. `/`, `/resume`, `/projects/[slug]`, `/sql` |
| 소스 | GitHub 단일 레포. 작업 단위 커밋. 매일 커밋(히트맵 = hardworker 증거) |
| 학습 병행 | SQLD = Oracle 문법 → Oracle Live SQL 별도 |

## 9. 참조 문서 (프로젝트 내)
- `S&O 직무 분석` — JD·면접·실제 업무
- `포트폴리오 마스터 플랜` — 전체 순서
- `분석 방법론 매핑` — McKinsey·DDDM·기법↔케이스
- `Revolut 인재상 매핑` — 가치 원문·Bar Raiser·STAR 8개
