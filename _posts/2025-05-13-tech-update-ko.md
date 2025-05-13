# 🛠️ 2025-05-13 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Image Pull Policy the way you always thought it worked!
이 블로그 글은 Kubernetes v1.33의 새로운 기능인 이미지 풀 정책에서의 보안 개선 사항을 설명합니다. 이전에는 `imagePullPolicy: IfNotPresent`가 보안 문제를 일으킬 수 있었는데, 이는 한 노드에 있는 다른 Pod가 비공개 이미지를 적절한 인증 없이 사용할 수 있게 되는 경우가 있었기 때문입니다. Kubernetes v1.33에서는 Kubelet이 Pod의 자격 증명을 확인한 후에만 이미지를 사용할 수 있도록 하여 이 문제를 해결했습니다. `imagePullPolicy: Never`와 `imagePullPolicy: Always`의 동작도 설명하며, 향후 계획으로는 성능 향상을 위한 캐싱 레이어 추가, 자격 증명 만료 지원 등이 포함되어 있습니다. 사용자는 이 기능을 활성화하여 테스트할 수 있으며, 더 깊이 있는 참여를 위해 Kubernetes 커뮤니티에 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/12/kubernetes-v1-33-ensure-secret-pulled-images-alpha/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
블로그 글 요약: 이번 블로그에서는 Spring의 팬들을 위해 Broadcom의 V Körbes와의 특별한 팟캐스트 대화를 소개합니다. V Körbes는 애플리케이션의 위와 아래에서 보안을 다루는 일을 하고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
제목: 모델 컨텍스트 프로토콜 보안: 컨테이너로 더욱 안전한 에이전트 기반 AI

요약: 모델 컨텍스트 프로토콜(MCP) 도구는 현재 주로 초기 수용자들에 의해 사용되고 있지만, 더 넓은 범위로의 채택이 가속화되고 있습니다. 이러한 성장과 함께 MCP 보안 문제도 더욱 시급해지고 있습니다. MCP 도구는 에이전트의 자율성을 높임으로써 에이전트의 행동과 사용자 기대 간의 불일치, 통제되지 않은 실행과 관련된 새로운 위험을 초래합니다. 이러한 시스템은 또한 새로운 유형의 보안 문제를 제기합니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 505: Structured Concurrency (5th Preview)
JEP 505는 JDK 25에 목표로 하고 있는 구조적 동시성의 다섯 번째 프리뷰에 관한 것입니다. 이 JEP는 자바 개발 키트(JDK)의 미래 버전에 구조적 동시성을 도입하여 동시 프로그래밍을 더 쉽게 관리하고 오류 처리를 개선하는 것을 목표로 합니다.
👉 [자세히 보기](https://inside.java/2025/05/12/jep505-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 블로그 글에서는 Go 1.24 버전에서 도입된 `testing.B.Loop` 기능을 통해 더 예측 가능한 벤치마킹을 수행하는 방법에 대해 설명합니다. 이 새로운 기능은 벤치마크 루프를 개선하여 코드의 성능을 보다 정확하게 측정할 수 있도록 합니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참여합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이며, 유지보수자들과의 대화에 참여할 수 있는 기회도 마련됩니다. 행사 기간 동안 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

