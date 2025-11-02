# 🛠️ 2025-11-02 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes 사용 시 흔히 발생하는 7가지 실수와 이를 피하는 방법에 대해 다루고 있습니다. 글쓴이는 초기 Kubernetes 사용 경험을 토대로 자주 저지른 실수를 공유하며, Kubernetes 사용자가 피해야 할 주요 함정을 설명합니다. 주요 내용은 다음과 같습니다:

1. **리소스 요청 및 제한 설정 누락**: Pod의 CPU 및 메모리 요구사항을 지정하지 않아 자원 부족이나 과도한 자원 사용 문제를 초래할 수 있습니다.
2. **Liveness 및 Readiness Probe 과소평가**: 컨테이너의 건강 상태를 체크하는 Probe를 설정하지 않아 애플리케이션 비정상 상태를 감지하지 못할 수 있습니다.
3. **컨테이너 로그에만 의존**: `kubectl logs` 명령어로만 로그를 확인하면 로그 손실 위험이 있습니다. 중앙 집중식 로그 관리 솔루션을 사용하는 것이 좋습니다.
4. **개발 및 프로덕션 환경 동일하게 처리**: 환경별로 다른 요구사항을 고려하지 않으면 성능 저하나 보안 문제를 초래할 수 있습니다.
5. **사용하지 않는 리소스 방치**: 사용하지 않는 리소스를 제거하지 않으면 클러스터 자원이 낭비되고 비용이 증가할 수 있습니다.
6. **네트워킹에 과도하게 심취**: Kubernetes의 기본 네트워킹을 이해하기 전에 복잡한 네트워킹 솔루션을 도입하면 문제 해결이 어려워질 수 있습니다.
7. **보안 및 RBAC 소홀**: 보안 설정을 제대로 하지 않으면 클러스터가 보안 위협에 노출될 수 있습니다.

글쓴이는 이러한 함정을 피함으로써 Kubernetes 사용 시 발생할 수 있는 불필요한 스트레스를 줄일 수 있다고 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC2 released
Spring Data 2025.1.0-RC2 버전이 출시되었습니다. 이 버전은 주로 Spring Framework RC3와 Spring HATEOAS RC2를 반영하며, Spring Data Commons에서 구조적 개선을 포함하고 있습니다. 전체 변경 사항은 릴리스 노트에서 확인할 수 있습니다. 정식 버전(GA)은 11월 중순에 출시될 예정이며, Spring Framework 7.0 출시와 맞춰 진행될 것입니다. 이번 RC2에는 Spring Data Commons, JPA, MongoDB, Neo4j, KeyValue, Apache Cassandra, LDAP, REST, Redis, Elasticsearch, Couchbase, Relational 등 다양한 모듈의 업데이트가 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/31/spring-data-2025-1-0-RC2-released)

## 🔹 Docker - Security Doesn’t Have to Hurt
블로그 글 "Security Doesn’t Have to Hurt"는 보안이 업무 도구 사용을 방해하지 않길 바라는 내용을 다루고 있습니다. 많은 사람들이 업무를 수행하려고 할 때 보안 도구가 필요한 AI 서비스의 사용을 차단하는 등의 문제를 겪습니다. 하지만 놀랍게도 보안 팀 역시 이러한 문제를 원치 않으며, 보안과 생산성을 조화롭게 유지하고자 합니다. 이는 보안 팀과 사용자가 협력하여 해결할 수 있는 문제라는 점을 강조하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/security-shadow-it-collaboration/)

## 🔹 Java - Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS
제목: 값 클래스 힙 평탄화 - JEP 401에서 기대할 것 #JVMLS

요약: Project Valhalla의 값 타입 평탄화 접근 방식이 크게 발전했습니다. 이는 값 타입의 의미에 대한 깊은 이해와 Java 언어 및 JVM에서의 도전 과제로 인해 이루어진 것입니다.
👉 [자세히 보기](https://inside.java/2025/10/31/jvmls-jep-401/)

## 🔹 Golang - The Green Tea Garbage Collector
블로그 글에서는 Go 1.25 버전에 새로 도입된 실험적인 가비지 컬렉터인 "Green Tea"에 대해 소개하고 있습니다. Green Tea 가비지 컬렉터는 메모리 관리 효율성을 향상시키고, 애플리케이션의 성능을 최적화하는 데 중점을 두고 있습니다. 이 새로운 가비지 컬렉터의 도입으로 인해 Go 언어는 더욱 효율적인 메모리 사용과 성능 개선을 기대할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

