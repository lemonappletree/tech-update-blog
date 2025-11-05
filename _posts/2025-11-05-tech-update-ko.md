# 🛠️ 2025-11-05 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 블로그 글에서는 Kubernetes를 사용하면서 흔히 겪는 7가지 실수와 이를 피하는 방법에 대해 설명하고 있습니다. Kubernetes는 강력하지만 복잡하기 때문에, 처음 시작할 때는 여러 가지 실수를 저지르기 쉽습니다. 

1. **리소스 요청과 제한 설정 누락**: Pod의 CPU 및 메모리 요구사항을 명시하지 않으면 리소스 부족이나 남용을 초래할 수 있습니다. 적절한 요구사항과 제한을 설정해 리소스 관리 효율을 높일 수 있습니다.

2. **활성 및 준비 상태 검사 과소평가**: 컨테이너의 상태를 확인하지 않으면 문제가 발생할 때 적절히 대처할 수 없습니다. 활성 및 준비 상태 검사를 설정하여 컨테이너의 건강 상태를 모니터링해야 합니다.

3. **컨테이너 로그에만 의존**: `kubectl logs` 명령어는 일시적인 해결책일 뿐입니다. 로그를 중앙 집중화하여 저장하고 분석할 수 있는 시스템을 구축하는 것이 중요합니다.

4. **개발 환경과 프로덕션 환경 동일하게 취급**: 환경별 요구사항을 무시하면 다양한 문제가 발생할 수 있습니다. 각 환경에 맞춘 설정이 필요합니다.

5. **오래된 리소스 방치**: 사용하지 않는 리소스를 방치하면 클러스터 리소스를 낭비하게 됩니다. 주기적으로 클러스터를 점검하고 불필요한 리소스를 정리해야 합니다.

6. **네트워킹에 대한 과도한 접근**: Kubernetes의 기본 네트워킹 기능을 이해하기 전에 복잡한 네트워킹 솔루션을 도입하면 문제 해결이 어려워질 수 있습니다.

7. **보안 및 RBAC 설정 소홀**: 보안 설정을 소홀히 하면 클러스터가 위험에 노출될 수 있습니다. RBAC를 통해 권한을 적절히 관리하고, 보안 설정을 강화해야 합니다.

이 글을 통해 Kubernetes의 복잡한 요소들을 이해하고, 실수를 피하며 효과적으로 관리하는 데 도움이 되기를 바랍니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring for GraphQL 2.0.0-RC2 released
Spring for GraphQL 2.0.0-RC2 버전이 출시되었습니다. 이번 릴리스는 GraphQL Java 25.x 버전을 기준으로 하며, 새로운 기능인 인터페이스 유형에 대한 `@EntityMapping` 지원을 포함하고 있습니다. 다음 달에 최종 릴리스가 예정되어 있으며, 관련 릴리스 노트는 위키에서 확인할 수 있습니다. 이번 버전은 Spring의 공식 저장소와 Maven Central에서 다운로드할 수 있습니다. 궁금한 점은 Stack Overflow의 `spring-graphql` 태그를 사용해 질문할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/04/spring-for-graphql-2-0-0-rc2-released)

## 🔹 Docker - How to Use Multimodal AI Models With Docker Model Runner
이 기술 블로그 글은 Docker Model Runner를 사용하여 멀티모달 AI 모델을 활용하는 방법에 대해 설명합니다. 멀티모달 AI 모델은 텍스트, 이미지, 오디오 등 다양한 유형의 입력을 이해하고 생성할 수 있는 능력을 가진 최신 AI 기술 중 하나입니다. 이러한 모델을 사용하면 단순히 텍스트 입력에만 의존하지 않고 이미지나 소리를 통해도 모델과 상호작용할 수 있습니다. 이 글에서는 Docker를 활용하여 이러한 멀티모달 AI 모델을 실행하고 활용하는 방법을 다루고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-use-multimodel-ai-with-model-runner/)

## 🔹 Java - Integrity by Default
"Integrity by Default"라는 제목의 기술 블로그 글은 Java 플랫폼이 성능, 이식성 및 보안을 지원하기 위해 추상화 구조와 프로그래머가 정의한 추상화를 더욱 견고하게 만들고, 불변성을 로컬에서 보장할 수 있는 상태로 발전하고 있다는 내용을 다루고 있습니다. 라이브러리는 애플리케이션이 선택적으로 허용하는 경우에만 일부 불변성을 위반할 수 있습니다. 이 세션에서는 "Integrity by Default"라는 비전의 이유와 방법을 설명합니다.
👉 [자세히 보기](https://inside.java/2025/11/04/javaone-integrity-by-default/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되었습니다. 이 기술 블로그 글에서는 Green Tea의 기능과 개선 사항에 대해 설명하고 있습니다. Green Tea는 메모리 관리 효율성을 높이고 가비지 컬렉션 작업의 성능을 향상시키기 위해 설계되었습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

