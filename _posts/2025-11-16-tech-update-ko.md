# 🛠️ 2025-11-16 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Kubernetes SIG Network와 Security Response Committee는 Ingress NGINX의 은퇴 계획을 발표했습니다. Ingress NGINX는 2026년 3월까지 유지보수가 이루어지며 이후에는 더 이상 릴리스, 버그 수정, 보안 업데이트가 제공되지 않습니다. 기존의 배포는 계속 작동하며, 설치 아티팩트도 이용 가능합니다. 사용자들에게는 Gateway API로의 전환을 권장하며, Kubernetes 문서에 나와 있는 다른 Ingress 컨트롤러들도 고려할 수 있습니다. Ingress NGINX는 Kubernetes 프로젝트 초기부터 많은 유연성과 기능으로 인기를 끌어왔지만, 유지보수 인력 부족으로 인해 지속 가능성이 없어 은퇴를 결정하게 되었습니다. Ingress NGINX 사용자는 즉시 Gateway API나 다른 Ingress 컨트롤러로의 마이그레이션을 시작할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Data 2025.0.6 and 2024.1.12 released
Spring Data 팀은 2025.0.6 및 2024.1.12 서비스 릴리스를 공개했습니다. 이번 릴리스에서는 의존성 업그레이드와 버그 수정이 포함되어 있습니다. 다음 주에 예정된 Spring Boot 릴리스에서 이 버전들이 포함될 예정입니다. 2025.0.6 버전에는 Spring Data Commons, JPA, MongoDB, Neo4j, KeyValue, Apache Cassandra, LDAP, REST, Redis, Elasticsearch, Couchbase, Relational이 포함되어 있으며, 각각의 문서와 변경 로그가 제공됩니다. 2024.1.12 버전도 마찬가지로 해당 기술 스택을 포함하고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/14/spring-data-2025-0-6-and-2024-1-12-released)

## 🔹 Docker - Making the Most of Your Docker Hardened Images Trial – Part 1
블로그 글 "Making the Most of Your Docker Hardened Images Trial – Part 1"은 Docker Hardened Images를 사용하여 안전한 프로덕션 준비 이미지 실행의 첫 단계를 설명합니다. 컨테이너 기반 이미지는 애플리케이션 보안의 기초가 되며, 취약점이 있는 경우 모든 서비스가 동일한 위험을 상속받게 됩니다. Docker Hardened Images는 이러한 문제를 해결하기 위해 지속적으로 유지 관리되는 최소한의 보안 중심 베이스 이미지를 제공합니다. 불필요한 패키지를 제거하고 적극적으로 패치를 적용하여 보안을 강화합니다.
👉 [자세히 보기](https://www.docker.com/blog/making-the-most-of-your-docker-hardened-images-trial-part-1/)

## 🔹 Java - Deep Dive into Gatherers - JEP Cafe #24
이 기술 블로그 글에서는 JDK 24에 추가되고 JDK 25에서 사용할 수 있는 Gatherers에 대해 자세히 다룬 내용을 소개합니다. Gatherers를 사용하여 매핑과 필터링의 기본 개념을 비롯해 내부 변경 가능한 상태를 생성하고 관리하여 스트림을 제한하거나 정렬하는 방법을 설명합니다. 또한, 스트림을 적절히 중단하는 방법, API 사용 시 리소스 누수와 경쟁 조건을 피하는 방법, 통합기를 필요에 따라 탐욕적으로 선언하여 최적화를 활용하는 방법도 설명합니다. 스트림 API의 가장 큰 장점 중 하나는 병렬 처리를 선택할 수 있다는 점인데, 병렬 Gatherers와 병렬 스트림에서의 비병렬 Gatherers 사용 방법도 다룹니다. 이 글을 통해 효율적이고 올바른 Gatherers 작성 방법과 언제 사용해야 하며 피해야 하는지를 배울 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/14/jepcafe24/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16번째 생일을 축하하는 내용입니다. 이 글에서는 Go 언어의 발전과 성과를 돌아보며, 커뮤니티와 기여자들에게 감사의 메시지를 전하고 있습니다. Go 언어는 지난 16년 동안 많은 개발자들에게 사랑받으며 성장해왔고, 앞으로도 지속적인 발전이 기대됩니다.
👉 [자세히 보기](https://go.dev/blog/16years)

