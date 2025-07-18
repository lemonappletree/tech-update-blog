# 🛠️ 2025-07-18 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 블로그 글은 양자 컴퓨터의 발전으로 인해 기존 암호화 표준을 깨트릴 가능성에 대비하기 위한 '양자 이후 암호화'(Post-Quantum Cryptography, PQC)에 대해 다루고 있습니다. 특히 Kubernetes 생태계에서 PQC의 상태와 그 의미를 설명합니다. 현재 TLS의 주요 암호화 작업인 키 교환과 디지털 서명에 대해 PQC가 적용되는 방식과 각기 다른 필요성과 타임라인을 설명합니다. 특히, 하이브리드 키 교환 메커니즘이 중요한 우선순위로 대두되고 있으며, Kubernetes v1.33에서는 Go 1.24를 사용하여 기본적으로 하이브리드 PQC 키 교환을 지원하게 됩니다. 그러나 Go 버전 불일치로 인해 발생할 수 있는 문제점과 패킷 크기 제한 같은 실질적인 문제도 존재합니다. 현재 PQC 디지털 서명의 채택은 초기 단계에 있으며, 이에 대한 표준화와 도구 체인 지원이 아직 부족한 상태입니다. Kubernetes의 양자 보안을 강화하기 위해서는 이러한 발전에 대한 지속적인 관심과 이해가 필요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring legends Tasha Isenberg and Jason Konicki
제목: A Bootiful Podcast: Spring 전설 Tasha Isenberg과 Jason Konicki
요약: 이 에디션에서는 뛰어난 API 전문가 Arjen Poutsma와 대화를 나누었습니다. 그의 통찰력과 생각, 그리고 컨설팅 서비스에 대해 궁금하다면 [poutsma-principles.com](https://poutsma-principles.com)을 확인해보세요.
👉 [자세히 보기](https://spring.io/blog/2025/07/17/a-bootiful-podcast-jason-and-tasha)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
이 기술 블로그 글은 GoFiber v3와 Testcontainers를 사용하여 외부 서비스에 의존하는 앱의 로컬 개발을 개선하는 방법을 설명합니다. 외부 서비스 의존성으로 인해 스크립트가 불안정해지고 환경이 일관되지 않을 수 있는데, Fiber v3와 Testcontainers는 이러한 문제를 해결합니다. 이들은 실제 서비스 의존성을 앱의 라이프사이클에 통합하여 관리가 용이하고, 재현 가능하며 개발자 친화적인 환경을 제공합니다. 다가오는 Fiber v3 릴리스에서는 더욱 강력한 기능이 도입될 예정입니다.
👉 [자세히 보기](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - Java Gets a JSON API - Inside Java Newscast #95
이 기술 블로그 글은 Java가 JSON API를 도입하려는 계획에 대해 다루고 있습니다. Java는 "배터리가 포함된" 언어로서, 데이터 교환 형식으로서의 JSON의 보편성을 고려할 때, JSON API가 필요하다고 판단하고 있습니다. 이 에피소드에서는 이러한 API 탐색을 시작하는 OpenJDK 이메일을 소개하며, Java가 JSON API를 구체화하려는 움직임을 설명하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/17/newscast-95/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
블로그 글 요약: Go 언어에 FIPS 140-3 표준을 준수하는 암호화 모드가 새롭게 내장되었습니다. 이는 Go에서 보안 요구 사항을 충족하는 데 도움이 되는 기능입니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회입니다. 대화 세션과 프로젝트 파빌리온 내 Helm 부스에서 유지 관리자들과 소통할 수 있으니 많은 참여 바랍니다. 주간 동안 진행될 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

