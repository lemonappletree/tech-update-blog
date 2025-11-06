# 🛠️ 2025-11-06 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes를 사용할 때 흔히 겪는 7가지 함정 및 이를 피하는 방법을 다룹니다. 주요 내용은 다음과 같습니다:

1. **리소스 요청 및 제한 설정 누락**: Pod의 CPU 및 메모리 요구사항을 명시하지 않으면, 자원 부족이나 과다 사용으로 인한 문제 발생 가능성이 큽니다. 초기에는 적절한 요청 값을 설정하고, 실제 사용량을 모니터링하며 조정해야 합니다.

2. **생존 및 준비 상태 검사 과소평가**: 컨테이너의 상태를 Kubernetes가 적절히 점검할 수 있도록 생존 및 준비 상태 검사를 정의해야 합니다. 이를 통해 컨테이너가 응답하지 않을 때 자동으로 재시작할 수 있습니다.

3. **컨테이너 로그에만 의존**: `kubectl logs` 명령어는 일시적인 로그만 제공하므로, 로그를 중앙에서 관리하고 OpenTelemetry 및 Prometheus와 같은 도구를 활용하여 전체적인 시스템 상태를 파악해야 합니다.

4. **개발과 운영 환경 동일하게 취급**: 환경별로 설정을 다르게 적용해야 합니다. Kustomize나 ConfigMaps 등을 사용하여 환경별 특성에 맞는 설정을 적용하는 것이 중요합니다.

5. **불필요한 리소스 방치**: 사용하지 않는 리소스를 제거하지 않으면 클러스터 자원을 낭비하게 됩니다. 정기적인 클러스터 점검과 자동화된 정책을 통해 이를 방지해야 합니다.

6. **네트워킹에 대한 과도한 초기 접근**: 복잡한 네트워크 솔루션을 도입하기 전에 Kubernetes의 기본 네트워킹을 충분히 이해해야 합니다. 작은 규모로 시작하여 필요할 때 확장하는 것이 좋습니다.

7. **보안 및 RBAC 소홀**: 컨테이너를 비루트 사용자로 실행하고, 이미지를 특정 버전으로 고정하며, RBAC를 통해 권한을 적절히 설정해야 보안 사고를 예방할 수 있습니다.

글의 마지막에서는 Kubernetes의 잠재력을 최대한 활용하기 위해서는 이러한 함정을 피하고, 실수로부터 배우는 것이 중요하다는 점을 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring gRPC Next Steps for 1.0.0
이 기술 블로그 글은 Spring gRPC 1.0.0에 대한 계획을 소개합니다. Spring gRPC를 Spring Boot 4와 통합하려는 계획이 있었으나 시간이 부족해 Spring Boot 4에 대한 지원을 현재의 Spring gRPC 프로젝트에 추가하기로 했습니다. Spring gRPC 1.0이 곧 출시될 예정이며, autoconfiguration은 Spring Boot 4.1의 초기 버전에 병합될 것으로 예상됩니다. 사용자는 의존성 관리에서 간단히 버전을 변경하여 업그레이드할 수 있습니다. Spring gRPC의 autoconfiguration 및 starter 의존성은 출시와 동시에 사용 중단(deprecated)될 예정입니다. 이러한 변화를 통해 프로젝트에 큰 혼란 없이 업그레이드할 수 있도록 지원합니다. Spring gRPC 1.0은 Spring Boot 4.0에 의존하게 되며, 0.x 버전을 사용 중인 프로젝트에는 최소한의 변화가 예상됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/11/spring-grpc-next-steps)

## 🔹 Docker - How to Use Multimodal AI Models With Docker Model Runner
이 블로그 글은 Docker Model Runner를 사용하여 멀티모달 AI 모델을 활용하는 방법에 대해 설명합니다. 멀티모달 지원은 현대 AI의 중요한 발전 중 하나로, 텍스트, 이미지, 오디오 등 여러 유형의 입력을 이해하고 생성할 수 있는 능력을 의미합니다. 이러한 모델을 통해 사용자는 단순히 텍스트 입력에만 의존하지 않고, 이미지를 보여주거나 소리를 재생하여 모델이 이를 이해하도록 할 수 있습니다. 이 글에서는 Docker Model Runner를 활용해 이러한 멀티모달 AI 모델을 어떻게 실행하고 활용할 수 있는지에 대해 다룹니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-use-multimodel-ai-with-model-runner/)

## 🔹 Java - JEP targeted to JDK 26: 522: G1 GC: Improve Throughput by Reducing Synchronization
이 기술 블로그 글은 JDK 26 버전에 목표를 두고 있는 JEP 522에 관한 내용입니다. JEP 522는 G1 가비지 컬렉터(GC)의 동기화를 줄여서 처리량을 개선하는 것을 목표로 하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/05/jep522-target-jdk26/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적인 가비지 컬렉터인 'Green Tea'가 포함되었습니다. 이 기술 블로그 글은 Green Tea 가비지 컬렉터의 도입과 그 특징에 대해 설명하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

