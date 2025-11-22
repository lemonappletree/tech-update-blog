# 🛠️ 2025-11-22 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
이 블로그 글에서는 Kubernetes의 SIG Network와 Security Response Committee가 Ingress NGINX의 은퇴를 발표했습니다. Ingress NGINX는 2026년 3월까지 유지 보수가 이루어지며 이후에는 더 이상 업데이트나 보안 취약점 해결이 이루어지지 않을 것입니다. 기존의 Ingress NGINX 배포는 계속 작동하며 설치 아티팩트도 이용 가능합니다. 사용자는 Gateway API 또는 다른 Ingress 컨트롤러로의 이전을 권장합니다. Ingress NGINX는 Kubernetes 프로젝트 초기에 개발된 API 구현의 예로, 유연성과 기능 덕분에 인기를 끌었습니다. 하지만 유지 관리의 어려움과 보안 문제로 인해 프로젝트가 종료됩니다. 사용자는 현재 사용 여부를 확인하고, 즉시 대체 옵션으로의 전환을 시작해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Modulith 2.0 GA, 1.4.5, and 1.3.11 released
이 기술 블로그 글은 Spring Modulith 2.0의 출시와 관련된 내용입니다. 이 릴리스는 Spring Modulith의 첫 번째 세대에서 얻은 모든 학습을 통합한 중요한 이정표입니다. 주요 기능으로는 이벤트 발행 라이프사이클의 전면 개편, 애플리케이션 모듈별 Flyway 마이그레이션 지원, 이벤트 외부화의 직렬 실행 허용, 이벤트 직렬화에서 Jackson 3 지원, 애플리케이션 모듈 구조의 시작 시 검증 지원 등이 포함됩니다. 또한, Spring Boot 4와 Framework 7로의 업그레이드가 이루어졌으며, 1.4 및 1.3 세대에 대한 버그 수정 릴리스도 포함되어 있습니다. 자세한 내용은 전체 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/21/spring-modulith-2-0-ga-1-4-5-and-1-3-11-released)

## 🔹 Docker - The Rising Importance of Governance at SwampUP Berlin 2025
블로그 글은 2025년 11월 12일부터 14일까지 열린 JFrog SwampUP Berlin 2025 행사에서 Docker 팀의 참여와 경험을 다루고 있습니다. Docker 팀은 다양한 기술 세션에 참여하고, 대화형 토론을 진행하며 참석자들과 많은 대화를 나누었습니다. JFrog 팀에게 감사의 인사를 전하며, 이번 행사에서 소프트웨어 거버넌스의 중요성에 대한 주요 배움을 공유하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/the-rising-importance-of-governance-at-swampup-berlin-2025/)

## 🔹 Java - Java 26 Warns of Deep Reflection - Inside Java Newscast #101
Java 26에서는 실행 시간에 리플렉션을 통해 final 필드가 변경될 때 경고를 발행합니다. 이는 미래에 기본적으로 이러한 final 필드 변경을 불법으로 만들어 Java의 무결성, 특히 final 키워드를 개선하기 위한 준비입니다. 이러한 변화는 유지보수성, 보안, 성능에 긍정적인 영향을 미칠 것입니다. final 필드 변경을 피하는 것이 권장되지만, 특정 모듈에 대해서는 새로운 영구 명령줄 옵션인 --enable-final-field-mutation을 통해 이를 허용할 수 있습니다. 또한, 마이그레이션을 쉽게 하기 위해 보다 일반적이지만 일시적인 옵션인 --illegal-final-field-mutation도 도입되었습니다.
👉 [자세히 보기](https://inside.java/2025/11/20/newscast-101/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16번째 생일을 축하하는 내용입니다. 글에서는 Go의 탄생 배경, 지난 16년간의 발전 과정, 그리고 Go 커뮤니티의 성장과 기여에 대해 이야기하고 있습니다. 또한, Go 언어가 개발자들에게 가져다준 효율성과 생산성의 향상에 대해서도 강조하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

