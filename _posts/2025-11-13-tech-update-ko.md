# 🛠️ 2025-11-13 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
이 블로그 글은 Kubernetes SIG Network와 Security Response Committee가 Ingress NGINX의 퇴역을 발표하는 내용을 담고 있습니다. Ingress NGINX는 2026년 3월까지 유지보수가 진행되며 이후에는 더 이상 릴리스나 버그 수정, 보안 취약점 해결 업데이트가 제공되지 않습니다. 현재 배포된 Ingress NGINX는 계속 작동하며 설치 아티팩트도 계속 이용할 수 있습니다. 사용자는 Gateway API와 같은 대안으로의 마이그레이션을 추천받고 있으며, Kubernetes 문서에는 여러 대안 Ingress 컨트롤러가 나열되어 있습니다. Ingress NGINX는 유연성과 많은 기능으로 인기를 끌었으나 유지보수의 어려움과 기술 부채 문제가 커져 왔습니다. 따라서 사용자 안전을 위해 프로젝트를 종료하기로 결정했습니다. SIG Network와 Security Response Committee는 모든 사용자가 즉시 Gateway API나 다른 Ingress 컨트롤러로의 마이그레이션을 시작할 것을 권장하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Null-Safe applications with Spring Boot 4
이 블로그 글은 Spring Boot 4에서 Null 안전성을 지원하는 방법을 설명합니다. "Road to GA" 시리즈의 일부로, Spring 포트폴리오 전반에 걸친 Null 안전성 지원 상태를 업데이트합니다. JSpecify와 NullAway를 사용해 Spring 애플리케이션에서 Null 안전성을 구현하며, 대부분의 Spring 포트폴리오 API가 Null 안전성을 제공하도록 설정했습니다. JetBrains의 IntelliJ IDEA와 같은 IDE는 JSpecify 주석을 지원하여 개발자가 Null 가능성 문제를 처리하는 데 도움을 줍니다. 또한, NullAway와 같은 빌드 타임 Null 검사를 사용해 애플리케이션의 NullPointerException 위험을 줄일 수 있습니다. JSpecify 주석을 도입하여 기존 코드베이스를 수정하지 않고도 타입 시스템에 Null 가능성을 명시적으로 표현할 수 있습니다. 이로 인해 Spring 코드베이스의 품질과 강건성이 향상되었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/12/null-safe-applications-with-spring-boot-4)

## 🔹 Docker - Docker Desktop 4.50: Indispensable for Daily Development
블로그 글 요약: Docker Desktop 4.50은 소프트웨어 개발, 보안, 배포 방식을 크게 발전시킨 버전입니다. 최근 몇 차례의 업데이트를 통해 개발자들이 매일 직면하는 문제들을 해결하기 위한 중요한 개선 사항들이 추가되었습니다. 예를 들어, 더 빠른 디버깅 워크플로우, 개발에 방해되지 않는 엔터프라이즈급 보안 제어, 그리고 현대적 개발을 위한 원활한 AI 통합 등이 포함됩니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-4-50/)

## 🔹 Java - The Inside Java Newsletter: The Latest on JavaOne 2026
제목: Inside Java 뉴스레터: JavaOne 2026의 최신 소식

요약: 2025년 10월자의 Inside Java 뉴스레터는 JavaOne 2026 준비에 초점을 맞추고 있습니다. 뉴스레터의 링크를 통해 업데이트를 구독하고, 2026년 3월에 만나보세요! 개발자, 학습자, 교육자 및 고객을 위한 멀티미디어 콘텐츠는 learn.java, dev.java, inside.java에서 확인할 수 있습니다. 뉴스레터 아카이브를 보고 구독하거나 친구에게 공유하세요!
👉 [자세히 보기](https://inside.java/2025/11/12/inside-java-newsletter/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 'Green Tea'가 포함되었습니다. 이 가비지 컬렉터는 메모리 관리의 효율성을 높이기 위해 도입되었습니다. 자세한 내용은 Go의 공식 블로그를 참고하세요.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

