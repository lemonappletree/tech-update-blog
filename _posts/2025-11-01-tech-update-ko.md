# 🛠️ 2025-11-01 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 블로그 글은 Kubernetes를 사용할 때 흔히 겪을 수 있는 7가지 함정과 이를 피하는 방법에 대해 설명합니다. Kubernetes는 강력하지만 때로는 좌절감을 줄 수 있으며, 처음 시작할 때 다양한 실수를 할 가능성이 높습니다. 이 글에서는 경험을 통해 배운 주요 함정과 이를 피하는 방법을 공유합니다.

1. **자원 요청 및 제한 설정 누락**: Pod 설정에서 CPU와 메모리 요구 사항을 명시하지 않으면 자원 부족 또는 과도한 자원 사용으로 인한 문제를 초래할 수 있습니다.

2. **활성 및 준비 상태 검사 과소평가**: 컨테이너의 건강 상태와 준비 상태를 확인하는 방법을 명확히 정의하지 않으면 예상치 못한 문제를 초래할 수 있습니다.

3. **컨테이너 로그에만 의존**: `kubectl logs` 명령어에만 의존하면 로그 손실의 위험이 있으므로 로그를 중앙 집중화해야 합니다.

4. **개발과 운영 환경을 동일하게 취급**: 환경별 요인을 고려하지 않고 동일한 설정을 사용하면 각 환경에서 문제를 일으킬 수 있습니다.

5. **오래된 리소스 방치**: 사용하지 않거나 구식인 리소스를 클러스터에 남겨두면 리소스 낭비와 혼란을 초래할 수 있습니다.

6. **네트워킹에 너무 깊이 빠져들기**: Kubernetes의 기본 네트워킹을 이해하지 않고 복잡한 네트워크 솔루션을 도입하면 문제 해결이 어려워집니다.

7. **보안 및 RBAC 과소평가**: 컨테이너를 비루트 사용자로 실행하는 등 보안 설정을 강화하지 않으면 보안 위험에 노출될 수 있습니다.

이 글은 이러한 함정을 피하는 것이 Kubernetes를 효과적으로 활용하는 데 중요하다고 강조하며, 공식 문서와 커뮤니티를 적극 활용할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Data 2025.1.0-RC2 released
이 블로그 글은 Spring Data의 다음 세대 두 번째 릴리스 후보(RC)를 발표하는 내용입니다. 이번 RC는 Spring Framework RC3와 Spring HATEOAS RC2를 포함하며, 주로 Spring Data Commons의 구조적인 정리 및 개선을 제공합니다. 전체 변경 사항은 Spring Data 2025.1 릴리스 노트에서 확인할 수 있습니다. 앞으로 Spring Data 2025.1 GA는 11월 중순에 Spring Framework 7.0 릴리스와 함께 출시될 예정입니다. 이번 릴리스 후보에는 여러 Spring Data 모듈(JPA, MongoDB, Neo4j 등)의 4.0 RC2 및 5.0 RC2 등이 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/31/spring-data-2025-1-0-RC2-released)

## 🔹 Docker - Security Doesn’t Have to Hurt
제목: 보안이 꼭 고통스러울 필요는 없다

요약: 보안이 업무에 필요한 도구 사용을 막지 않았으면 좋겠다고 생각해 본 적이 있나요? 사실 보안팀도 같은 생각을 하고 있습니다. 업무를 마치려고 할 때, 문서를 번역하는 데 필요한 AI 서비스가 보안 웹 모니터링 도구에 의해 차단되는 상황이 발생할 수 있습니다. 이와 같은 문제는 보안팀과 협력하여 해결할 수 있으며, 보안과 생산성 모두를 만족시키는 방법을 찾아야 한다고 강조합니다.
👉 [자세히 보기](https://www.docker.com/blog/security-shadow-it-collaboration/)

## 🔹 Java - Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS
블로그 글 요약: JEP 401에 관한 이 글은 Project Valhalla에서의 값 타입 평탄화(flattening)의 진화된 접근 방식을 다룹니다. 값 타입의 의미론에 대한 깊은 이해와 Java 언어 및 JVM에서의 도전 과제들이 이러한 변화의 원동력이 되었습니다. 이로 인해 값 타입을 다루는 새로운 방식이 개발되고 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/31/jvmls-jep-401/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되었습니다. 이 블로그 글에서는 Green Tea 가비지 컬렉터의 특징과 작동 방식에 대해 설명하고 있습니다. Green Tea는 메모리 관리의 효율성을 높이고 성능을 개선하기 위해 설계되었습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

