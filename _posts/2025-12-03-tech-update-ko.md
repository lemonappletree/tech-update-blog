# 🛠️ 2025-12-03 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
이 기술 블로그 글은 다가오는 Kubernetes v1.35 릴리스에 대한 주요 변경 사항 및 새로운 기능들을 소개합니다. 주요 내용은 다음과 같습니다:

1. **지원 중단 및 제거**: 
   - cgroup v1 지원이 더 이상 되지 않으며, 이를 위해 Linux 노드를 cgroup v2를 지원하는 시스템으로 마이그레이션해야 합니다.
   - kube-proxy의 ipvs 모드가 더 이상 지원되지 않으며, 권장 모드는 nftables입니다.
   - containerd v1.y 지원이 중단되며, 이후 버전에서는 containerd 2.0 이상을 사용해야 합니다.

2. **주요 개선 사항**:
   - 노드 선언 기능: 노드가 지원하는 Kubernetes 기능을 명시적으로 선언하여 스케줄링의 정확성을 높이고, 클러스터 안정성을 향상시킵니다.
   - Pod 리소스 현장 업데이트: Pod나 Container를 재시작하지 않고 cpu 및 메모리 리소스를 조정할 수 있어, 효율성을 높이고 작업 중단을 최소화합니다.
   - Pod 인증서: mTLS를 위한 강력한 암호화 인증서를 Pods에 자동으로 제공하여 보안성을 강화합니다.
   - 수치적 taint 값: taint와 toleration에 수치 비교 연산자를 도입하여, 수치적 조건을 바탕으로 스케줄링을 최적화합니다.
   - 사용자 네임스페이스: 컨테이너의 루트 사용자를 호스트의 비특권 사용자로 재매핑하여 보안을 강화합니다.
   - OCI 이미지를 볼륨으로 마운트: OCI 레지스트리의 데이터를 직접 볼륨으로 마운트하여, 데이터와 컨테이너 이미지를 분리할 수 있습니다.

Kubernetes v1.35 릴리스는 2025년 12월 17일에 예정되어 있으며, 최신 업데이트를 위해 Kubernetes 커뮤니티에 참여할 수 있는 다양한 방법도 소개하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - This Week in Spring - December 2nd, 2025
이번 주 Spring 블로그 글은 다양한 최신 소식을 소개합니다. 주요 내용으로는 Spring AI 1.1.0 RC1 출시, Spring Boot 4.0.0 RC2 및 Spring Tools 4.32.2 출시가 포함됩니다. 또한, Micrometer 1.16.0과 Micrometer Tracing 1.6.0 GA 버전이 공개되었고, Spring Batch 6.0.0-RC2와 Spring for GraphQL 2.0.0-RC2도 소개되었습니다. 이 외에, Spring 커뮤니티의 Simon Martinelli가 제안한 Spring Data의 `Page` 대신 `Slice`를 사용하는 대안 프로젝트와 관련된 내용도 다루고 있습니다. 추가적으로, 여러 컨퍼런스에서 Spring의 중요성을 알리기 위한 발표 일정도 공유되었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/12/02/this-week-in-spring-december-2nd-2025)

## 🔹 Docker - Building AI agents shouldn’t be hard. According to theCUBE Research, Docker makes it easy
이 기술 블로그 글은 AI 에이전트를 구축하는 것이 여전히 많은 개발자들에게 복잡하지만 Docker가 이를 쉽게 만든다는 내용을 다루고 있습니다. 다양한 모델, 도구, 플랫폼이 항상 잘 맞지 않는 상황에서 Docker는 표준화되고 이동 가능하며 확장 가능한 AI 환경을 위한 필수 인프라로 부상하고 있습니다. Docker는 구성 가능성, 단순성, GPU 접근성을 제공하여 에이전트 시대에 개발자들이 AI 개발을 더 쉽게 할 수 있도록 돕고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/building-ai-agents-shouldnt-be-hard-according-to-thecube-research-docker-makes-it-easy/)

## 🔹 Java - JEP targeted to JDK 26: 529: Vector API (11th Incubator)
제목이 "JEP 대상 JDK 26: 529: 벡터 API (11번째 인큐베이터)"인 기술 블로그 글은 JDK 26에 도입될 예정인 JEP 529, 즉 벡터 API의 11번째 인큐베이션에 대한 내용을 다루고 있습니다. 이 JEP는 벡터 연산을 위한 API를 제공하여 성능을 향상시키고, 개발자가 하드웨어 벡터 명령어를 더 쉽게 활용할 수 있도록 돕는 것을 목표로 하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/12/02/jep529-target-jdk26/)

## 🔹 Golang - Go’s Sweet 16
고 언어 16주년을 맞이하여 기념하는 글입니다. 이 글에서는 Go 언어의 발전과 성과를 되돌아보며, 커뮤니티의 기여와 앞으로의 방향에 대해 이야기합니다.
👉 [자세히 보기](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
기술 블로그 글 요약: 11월 12일 수요일, KubeCon + CloudNativeCon 행사에서 Helm 4 발표 중 Helm v4.0.0이 출시되었습니다. 이번 릴리스는 6년 만에 처음으로 나온 Helm의 새로운 메이저 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-4-released)

