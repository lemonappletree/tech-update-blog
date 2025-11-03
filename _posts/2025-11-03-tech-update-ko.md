# 🛠️ 2025-11-03 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes 사용 시 흔히 겪을 수 있는 7가지 함정과 이를 피하는 방법을 다룹니다. Kubernetes는 강력하지만 때로는 좌절감을 줄 수 있습니다. 글쓴이는 컨테이너 오케스트레이션을 처음 다루면서 많은 실수를 했고, 이를 통해 배운 교훈을 공유하고자 합니다.

1. 자원 요청 및 제한 설정을 생략하면, Pod가 필요 이상으로 자원을 소비하거나 충분한 자원을 받지 못해 성능 저하나 실패를 초래할 수 있습니다.
2. 라이브니스 및 레디니스 프로브를 과소평가하면, 애플리케이션이 비정상인데도 Kubernetes가 정상으로 판단할 수 있습니다.
3. 컨테이너 로그에만 의존하면, 로그가 손실될 위험이 있습니다. 중앙 집중화된 로그 시스템을 사용하는 것이 좋습니다.
4. 개발 환경과 프로덕션 환경을 동일하게 취급하면, 환경별 요구사항을 반영하지 못해 문제가 발생할 수 있습니다.
5. 오래된 리소스를 방치하면, 불필요한 자원 소모와 혼란을 초래할 수 있습니다.
6. 네트워킹에 지나치게 빨리 깊이 들어가면, 문제 해결이 어려워질 수 있습니다.
7. 보안과 RBAC를 가볍게 다루면, 보안 위협에 노출될 수 있습니다.

이 글은 Kubernetes의 공식 문서를 참고하여 더 깊이 있는 학습을 권장하고, 자신의 경험을 공유하며 커뮤니티와 협력할 것을 제안합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC2 released
이 블로그 글은 Spring Data 2025.1.0-RC2의 두 번째 릴리스 후보를 발표하는 내용입니다. 이 릴리스는 주로 Spring Framework RC3와 Spring HATEOAS RC2를 포함하며, Spring Data Commons의 구조적 정리를 포함한 주된 개선 사항을 제공합니다. 전체 변경 사항은 Spring Data 2025.1 릴리스 노트에서 확인할 수 있습니다. 앞으로 Spring Data 2025.1 GA는 11월 중순에 Spring Framework 7.0 릴리스와 함께 출시될 예정입니다. 각 프로젝트별로 Javadoc, 문서 및 변경 로그 링크가 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/31/spring-data-2025-1-0-RC2-released)

## 🔹 Docker - Security Doesn’t Have to Hurt
블로그 글 "Security Doesn’t Have to Hurt"는 보안 조치가 업무에 필요한 도구 사용을 방해하는 상황에 대한 내용을 다룹니다. 보안 팀 역시 업무 효율성을 저해하지 않는 보안을 원하고 있습니다. 예를 들어, 문서를 번역하기 위해 AI 서비스를 사용해야 하지만 보안 웹 모니터링 도구가 이를 차단하는 상황이 발생할 수 있습니다. 이 글은 보안과 업무 효율성 간의 균형을 찾기 위한 협력의 중요성을 강조합니다.
👉 [자세히 보기](https://www.docker.com/blog/security-shadow-it-collaboration/)

## 🔹 Java - Supercharge your JVM Performance with Project Leyden and Spring Boot
블로그 글 요약: 현대의 많은 애플리케이션과 도구들이 Java에 의존하고 있지만, 특히 마이크로서비스와 Kubernetes 워크로드의 빠른 확장성과 응답성을 위해 필요한 빠른 시작 시간과 최고 성능 도달 시간이 여전히 도전 과제입니다. 이러한 성능 병목 현상을 극복하기 위해 OpenJDK의 야심 찬 프로젝트인 Leyden이 추진되고 있습니다. 이 세션에서는 Ana와 Moritz가 Java 25와 Spring Boot를 활용하여 Leyden의 최적화를 어떻게 활용할 수 있는지 보여줍니다. 또한 Leyden 내부에서 진행 중인 작업과 이를 통해 Java 애플리케이션의 성능이 어떻게 향상될 수 있는지에 대한 실질적인 기술과 미래 전망도 제공합니다.
👉 [자세히 보기](https://inside.java/2025/11/02/devoxxbelgium-leyden-supercharge-jvm-performance/)

## 🔹 Golang - The Green Tea Garbage Collector
"Green Tea Garbage Collector"라는 제목의 기술 블로그 글은 Go 1.25 버전에 새롭게 실험적인 가비지 컬렉터인 Green Tea가 포함되었음을 소개합니다. 이 새로운 가비지 컬렉터는 메모리 관리의 효율성을 개선하고, 성능 향상을 목표로 하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

