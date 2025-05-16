# 🛠️ 2025-05-16 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes 1.33: Job's SuccessPolicy Goes GA
Kubernetes 1.33 버전에서 Job의 성공 정책이 일반 가용성(GA) 단계로 승격되었습니다. 이 정책은 배치 작업에서 리더-팔로워 패턴을 사용하는 경우 유용합니다. 성공 정책을 사용하면 일부 인덱스가 실패하더라도 전체 작업이 성공으로 간주될 수 있습니다. 이는 과학적 시뮬레이션, AI/ML 및 고성능 컴퓨팅(HPC) 배치 작업에 특히 유용합니다. 사용자는 `.spec.successPolicy` 필드를 통해 조기 종료 기준을 지정할 수 있으며, 특정 인덱스가 성공하면 Job이 성공으로 표시되고 모든 Pod가 종료됩니다. 이 기능은 Kubernetes의 배치 작업 그룹과 SIG Apps 커뮤니티의 협력으로 개발되었습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/15/kubernetes-1-33-jobs-success-policy-goes-ga/)

## 🔹 Spring Boot - Spring Web Services 4.0.14 available now
Spring Web Services 4.0.14 버전이 출시되어 Maven Central에서 이용 가능합니다. 이번 릴리스에는 1개의 종속성 업그레이드가 포함되어 있으며, 이슈 보고 및 풀 리퀘스트로 기여한 모든 분들께 감사드립니다. 기여를 원하시는 분들은 GitHub의 '기여에 이상적' 태그가 붙은 이슈를 확인하시기 바랍니다. 일반적인 질문은 Stack Overflow의 spring-ws 태그를 사용해 문의할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/15/spring-ws-4-0-14-available-now)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
블로그 글 제목은 "Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation"입니다. 이 글에서는 2025년 Microsoft Build 행사에서 Docker가 개발자 경험, 보안, AI 혁신을 어떻게 융합하는지를 소개합니다. Docker는 최신 제품 발표를 통해 팀이 현대 애플리케이션을 구축, 보안, 확장하는 방식을 새롭게 정의하고자 합니다. 이 행사는 시애틀 컨벤션 센터에서 직접 참석하거나 온라인으로 시청할 수 있으며, Docker의 개발자들을 위한 비전을 확인할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Mastering JVM Memory Troubleshooting - From OutOfMemoryErrors to Leaks
블로그 글 "JVM 메모리 문제 해결 마스터하기 - OutOfMemoryErrors에서 메모리 누수까지"는 Java 애플리케이션에서 발생할 수 있는 메모리 문제를 다룹니다. 이러한 문제는 진단하기 어려운 경우가 많으며, 자바 힙 고갈, 메타스페이스 초과, 네이티브 메모리 누수와 같은 일반적이거나 잘 알려지지 않은 다양한 메모리 문제를 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/05/15/javaone-jvm-troubleshooting/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24 버전에서 도입된 `testing.B.Loop` 기능에 대해 설명하고 있습니다. 이 기능은 벤치마크 테스트를 보다 예측 가능하게 만들어줍니다. `testing.B.Loop`를 사용하면 벤치마크 루프의 반복 횟수를 직접 제어할 수 있어 테스트의 일관성과 신뢰성을 높일 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 Helm

요약: Helm 팀이 올해도 KubeCon + CloudNativeCon EU '25에 참가하기 위해 영국 런던으로 향합니다. 이번 행사는 4월 1일부터 4일까지 진행됩니다. 올해 후반에 출시 예정인 Helm 4에 대한 논의를 위해 유지 관리자들과의 대화에 참여하고, Project Pavilion의 Helm 부스도 방문해 보세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 확인하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

