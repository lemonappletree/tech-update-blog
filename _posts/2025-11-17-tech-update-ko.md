# 🛠️ 2025-11-17 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Ingress NGINX의 은퇴가 발표되었습니다. Kubernetes SIG Network와 보안 대응 위원회는 Ingress NGINX의 유지를 2026년 3월까지 최선의 노력으로 계속할 것이며, 그 이후에는 더 이상의 릴리스, 버그 수정, 보안 취약점 업데이트가 제공되지 않을 것이라고 발표했습니다. 기존 Ingress NGINX 배포는 계속 작동하며 설치 아티팩트도 계속 제공됩니다. 사용자들에게는 Gateway API나 다른 Ingress 컨트롤러로의 마이그레이션을 권장합니다. Ingress NGINX는 Kubernetes 프로젝트 초기에 개발된 Ingress 컨트롤러로, 유연성과 기능 덕분에 인기를 끌었습니다. 그러나 유지 관리의 어려움과 보안 문제로 인해 프로젝트가 종료되며, 사용자는 대체 솔루션으로 이동해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Data 2025.0.6 and 2024.1.12 released
이 기술 블로그 글에서는 Spring Data의 두 가지 서비스 릴리스, 2025.0.6과 2024.1.12가 발표되었음을 알리고 있습니다. 이 릴리스들은 의존성 업그레이드와 버그 수정이 포함되어 있습니다. 향후 Spring Boot 릴리스는 다음 주까지 이 업데이트를 반영할 예정입니다. 각 버전은 Spring Data Commons, Spring Data JPA, Spring Data MongoDB 등 다양한 모듈에 대한 업데이트를 포함하고 있으며, 각각의 Javadoc, 문서 및 변경 로그에 대한 링크가 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/14/spring-data-2025-0-6-and-2024-1-12-released)

## 🔹 Docker - Making the Most of Your Docker Hardened Images Trial – Part 1
이 기술 블로그 글은 Docker Hardened Images를 활용하여 첫 번째 보안, 프로덕션 준비가 완료된 이미지를 실행하는 방법에 대해 설명합니다. 컨테이너 베이스 이미지는 애플리케이션 보안의 기초를 이루며, 이 기초에 취약점이 있을 경우, 그 위에 구축된 모든 서비스가 동일한 위험을 안게 됩니다. Docker Hardened Images는 이러한 문제를 근본적으로 해결하기 위해 설계된 지속적으로 유지 관리되는 최소한의 베이스 이미지로, 불필요한 패키지를 제거하고 사전적으로 패치를 적용하여 보안을 강화합니다.
👉 [자세히 보기](https://www.docker.com/blog/making-the-most-of-your-docker-hardened-images-trial-part-1/)

## 🔹 Java - Beyond the Vector API - A Quest for a Lower Level API #JVMLS
이 기술 블로그 글은 Vector API의 성능과 플랫폼 간 API 제공의 균형을 맞추려는 노력에 대해 다루고 있습니다. Vector API는 성공적이었지만, 설계에 맞지 않는 중요한 기능을 포기해야 했고, 이는 특정 하드웨어 기능에 의존하는 벡터화 알고리즘의 구현에 부적합하게 만들었습니다. Project Panama의 최근 발전(외부 함수 및 메모리 API와 jextract)으로 Java를 하드웨어에 더 가깝게 할 수 있는 새로운 기회가 생겼습니다. 이 강연에서는 Vector API가 어떻게 발전해왔는지 설명하고, Java 코드가 개별 기계 코드 명령에 접근할 수 있는 새로운 접근 방식을 소개합니다. 이러한 "하드웨어 고유 기능" API는 Vector API를 보완하며, Java 플랫폼에 새로운 기회를 열고 Vector API, JDK 및 JVM 구현의 단순화를 가능하게 합니다.
👉 [자세히 보기](https://inside.java/2025/11/16/jvmls-vector-api/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16주년을 기념하는 내용입니다. 글에서는 Go 언어의 발전과 성과를 돌아보고, 커뮤니티의 기여와 앞으로의 계획에 대해 이야기합니다. Go 언어는 효율성과 간결함으로 많은 개발자들에게 사랑받고 있으며, 지속적인 업데이트와 개선을 통해 계속해서 성장하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

