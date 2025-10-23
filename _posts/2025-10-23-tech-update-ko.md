# 🛠️ 2025-10-23 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 블로그 글은 Kubernetes를 사용할 때 자주 발생하는 7가지 함정을 소개하고, 이를 피하는 방법에 대한 팁을 제공합니다. Kubernetes는 강력하지만 때로는 복잡하여 실수를 유발할 수 있습니다. 주요 함정으로는 리소스 요청 및 제한을 생략하는 것, 라이브니스 및 레디니스 프로브를 과소평가하는 것, 로그 관리를 소홀히 하는 것, 개발 환경과 프로덕션 환경을 동일하게 취급하는 것, 오래된 리소스를 방치하는 것, 네트워킹을 과도하게 심화하는 것, 그리고 보안과 RBAC 설정을 소홀히 하는 것이 있습니다. 각 함정에 대한 상세한 설명과 이를 피하는 방법을 다루며, 실제 경험을 바탕으로 한 교훈도 공유합니다. Kubernetes를 처음 접하거나 이미 사용 중인 사용자에게 도움이 되는 통찰력을 제공하는 것이 이 글의 목적입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Batch 6.0.0-RC1 is out!
Spring Batch 6.0.0-RC1이 출시되었습니다. 이 릴리스 후보에는 다음과 같은 기능과 개선 사항이 포함되어 있습니다:

1. 우아한 종료 지원: 실행 중인 배치 작업을 중단할 때 안정적으로 종료할 수 있는 기능을 제공합니다.
2. 로컬 청킹 지원: 여러 스레드를 사용하여 대량의 항목을 병렬로 처리할 수 있는 기능을 제공합니다.
3. Spring Integration 메시지 채널을 사용한 SEDA 스타일: 메시지 채널을 통해 비동기적으로 배치 작업의 여러 단계를 처리할 수 있습니다.
4. Jackson 3 지원: 최신 Jackson 3.x 버전을 지원하여 성능과 보안을 향상시킵니다.
5. 원격 스텝 지원: 원격 기기나 클러스터에서 배치 작업의 단계를 실행할 수 있는 기능을 추가했습니다.

자세한 변경 사항은 릴리스 노트를 참조하세요. Spring Batch 6.0에 대한 피드백은 GitHub Issues, Discussions, 및 X에서 받을 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/22/spring-batch-6-0-0-rc1-released)

## 🔹 Docker - Getting Started with Offload: Automating Everyday Workflows with Docker
"Getting Started with Offload: Automating Everyday Workflows with Docker"라는 기술 블로그 글은 개발자들이 로컬 머신의 한계를 극복하기 위해 Docker를 활용하는 방법을 다룹니다. AI 모델을 훈련하거나, 대규모 코드베이스를 컴파일하거나, GPU 작업을 실행할 때 로컬 머신의 성능 제약으로 인해 작업이 느려질 수 있습니다. 이 글은 이러한 문제를 해결하기 위해 Docker를 사용하여 워크플로우를 자동화하고, 효율성을 높이는 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/getting-started-docker-offload/)

## 🔹 Java - HTTP/3 Support in JDK 26
JDK 26의 새로운 기능 중 하나로 `HttpClient`가 HTTP/3를 지원하게 되었습니다. `HttpClient`는 JDK 11부터 Java SE의 일부였으며, 이번 업데이트를 통해 최신 프로토콜을 사용할 수 있게 되었습니다.
👉 [자세히 보기](https://inside.java/2025/10/22/http3-support/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 "비행 기록" 기능이 도입되었습니다. 이 기능은 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 문제를 분석하고 디버깅하는 데 도움을 줍니다. 자세한 내용은 Go 공식 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글 "Helm Turns 10"은 Helm의 10주년을 기념하는 내용입니다. Helm은 10년 전 Kubernetes 1.1.0 출시 직후 해커톤에서 처음 탄생했습니다. 최초의 커밋은 Helm v1 코드베이스가 있는 helm-classic Git 저장소에서 확인할 수 있습니다. 초기 Helm은 Deployment Manager와 통합되고 Kubernetes 프로젝트에 포함되기 전의 것입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

