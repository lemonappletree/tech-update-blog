# 🛠️ 2025-08-20 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 기술 블로그 글은 Kubernetes v1.34 릴리스에서 안정 버전으로 예상되는 NodeSwap 기능에 대해 설명합니다. 이 기능은 물리적 RAM이 부족할 때 Linux 노드가 추가 가상 메모리로 스왑을 사용할 수 있게 하여 자원 활용을 개선하고 OOM(Out of Memory) 킬을 줄이는 것을 목표로 합니다. 그러나 스왑을 활성화하는 것은 단순한 해결책이 아니며, 리눅스 커널의 여러 매개변수 설정이 성능과 안정성에 큰 영향을 미칩니다. 잘못된 설정은 성능 저하와 Kubelet의 퇴거 로직에 간섭을 일으킬 수 있습니다.

글은 스왑 동작을 조정하는 중요한 리눅스 커널 매개변수에 대해 자세히 설명하고, 이들이 Kubernetes 워크로드 성능 및 스왑 활용에 미치는 영향을 탐구합니다. 또한, 다양한 테스트 결과를 통해 최적의 설정을 찾는 방법을 공유합니다. 블로그는 스왑 조정을 위한 시작점을 제시하며, 각자의 워크로드에 맞게 벤치마크 테스트를 수행할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Authorization Server 2.0.0-M2, 1.5.2 and 1.4.5 available now
Spring Authorization Server의 새로운 버전 2.0.0-M2, 1.5.2, 1.4.5가 출시되었습니다. 자세한 내용은 각 버전의 릴리스 노트를 참고하세요. Spring Authorization Server를 시작하려면 레퍼런스 문서의 시작 가이드와 샘플을 통해 설정과 구성 방법을 익힐 수 있습니다. 프로젝트 페이지와 GitHub 이슈 페이지도 함께 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/08/19/spring-authorization-server-2-0-0-M2-1-5-2-and-1-4-5-available-now)

## 🔹 Docker - Streamline NGINX Configuration with Docker Desktop Extension
이 기술 블로그 글은 Docker Desktop Extension을 사용하여 NGINX 설정을 간소화하는 방법에 대해 설명합니다. 글은 Docker 파트너와 실무자들의 성공 사례를 다루며, Dylen Turnbull과 Timo Stark가 기여했습니다. Dylen Turnbull은 Symantec, Veritas, F5 Networks에서의 경험을 바탕으로 현재 NGINX의 개발자 옹호자로 활동하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/streamline-nginx-configuration-with-docker-desktop-extension/)

## 🔹 Java - Auto-Vectorization in HotSpot #JVMLS
이 기술 블로그 글은 HotSpot C2의 자동 벡터화 기능에 대한 개발과 개선을 다룹니다. SuperWord 알고리즘에 대한 간단한 소개 이후, 발표자는 이미 달성된 주요 개선 사항을 설명하고, 실제 사례와 벤치마크를 통해 향후 발전 계획을 제시합니다.
👉 [자세히 보기](https://inside.java/2025/08/16/jvmls-hotspot-auto-vectorization/)

## 🔹 Golang - Go 1.25 is released
Go 1.25가 출시되었습니다. 이번 버전에서는 컨테이너 인식 GOMAXPROCS, testing/synctest 패키지, 실험적인 GC, 실험적인 encoding/json/v2 등 여러 기능이 추가되었습니다.
👉 [자세히 보기](https://go.dev/blog/go1.25)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 대화에 참여하고, 토크 세션 및 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 만날 수 있습니다. 주간 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

