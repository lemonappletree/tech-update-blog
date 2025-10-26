# 🛠️ 2025-10-26 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 기술 블로그 글은 Kubernetes를 사용할 때 흔히 저지르는 7가지 실수와 이를 피하는 방법에 대해 설명합니다. 첫 번째 실수는 리소스 요청 및 제한을 설정하지 않는 것으로, 이는 클러스터 관리에 중요한 역할을 합니다. 두 번째는 라이브니스 및 레디니스 프로브를 과소평가하는 것으로, 이는 컨테이너의 상태를 모니터링하는 데 필수적입니다. 세 번째는 컨테이너 로그에만 의존하는 것이며, 로그의 중앙 집중화가 필요합니다. 네 번째는 개발과 운영 환경을 동일하게 취급하는 것이며, 환경별 설정을 조정해야 합니다. 다섯 번째는 오래된 리소스를 제거하지 않는 것이며, 정기적인 클러스터 점검이 필요합니다. 여섯 번째는 네트워킹에 너무 깊이 들어가는 것이며, 기본적인 네트워킹 이해가 선행되어야 합니다. 마지막으로, 보안 및 RBAC를 소홀히 하는 것으로, 명확한 보안 정책이 필요합니다. 이 글은 이러한 실수를 피함으로써 Kubernetes 사용 시 발생할 수 있는 문제를 많이 줄일 수 있다고 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring Shell 4.0.0-M1 is available!
Spring Shell 4.0.0-M1이 Maven Central에 출시되었습니다. 이번 마일스톤 릴리스는 Spring Framework 7 및 Spring Boot 4와의 정렬을 목표로 하고 있으며, Spring Framework 7.0.0-RC2 및 Spring Boot 4.0.0-RC1을 기반으로 합니다. 11월에 Spring Shell 4.0의 GA 버전을 출시할 계획이며, 그 전까지 몇 가지 마일스톤과 릴리스 후보를 배포할 예정입니다. 주요 변경 사항으로는 jSpecify로의 nullability 어노테이션 및 체크 마이그레이션, 프로젝트 모듈화 개선, JUnit 6으로의 테스트 인프라 업데이트 등이 포함됩니다. 피드백은 GitHub Issues와 Discussions에서 받을 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/24/spring-shell-4-0-0-m1-released)

## 🔹 Docker - Docker Hub Incident Report – October 20, 2025
2025년 10월 20일, AWS의 US-East-1 지역에서 발생한 광범위한 장애로 인해 Docker Hub에 상당한 중단이 발생했습니다. 전 세계 개발자들이 하루 일과의 일부로 Docker를 사용하고 있기 때문에 이로 인한 불편을 사과드립니다. 이 블로그 글에서는 사건의 경과, 우리가 배운 점, 그리고 앞으로의 개선 방안에 대해 투명하게 공유하고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-hub-incident-report-october-20-2025/)

## 🔹 Java - Writing GPU-Ready AI Models in Pure Java with Babylon
Project Babylon은 개발자가 LLM, 이미지 분류기, 객체 감지 알고리즘과 같은 AI 모델을 Java에서 직접 빌드하고 실행할 수 있도록 합니다. 코드 리플렉션을 통해 기계 학습 로직을 일반 Java 코드로 정의할 수 있으며, Python이나 외부 모델 파일이 필요하지 않습니다. Foreign Function and Memory (FFM) API를 활용하여, Babylon은 Java 코드를 ONNX와 같은 네이티브 런타임에 연결하여 빠른 GPU 가속 추론을 제공합니다. 또한, Heterogeneous Accelerator Toolkit (HAT)을 통해 개발자는 Java에서 컴퓨트 커널을 작성하고 구성할 수 있어, Java 라이브러리가 고성능 컴퓨팅을 위해 GPU 성능을 쉽게 활용할 수 있게 합니다. 이 세션에서는 Babylon의 새로운 기능을 소개하고, Java 생태계에 AI 기능을 통합하는 방법을 보여줍니다. 이는 Java 애플리케이션에 AI를 통합하려는 라이브러리 유지 관리자 및 개발자 모두에게 유용합니다.
👉 [자세히 보기](https://inside.java/2025/10/25/devoxxbelgium-writing-gpuready-ai-models-in-java/)

## 🔹 Golang - Flight Recorder in Go 1.25
블로그 글 요약: Go 1.25 버전에서는 새로운 진단 도구인 플라이트 레코더가 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여, 개발자들이 문제를 쉽게 분석하고 디버깅할 수 있도록 돕습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글 "Helm Turns 10"는 Helm이 탄생한 지 10주년을 기념하는 내용입니다. Helm은 10년 전, Kubernetes 1.1.0이 출시된 직후 해커톤에서 처음으로 개발되었습니다. 초기 커밋은 2015년 10월 19일에 이루어졌으며, Helm v1의 코드베이스는 helm-classic Git 저장소에서 확인할 수 있습니다. Helm은 이후 Deployment Manager와 통합되어 Kubernetes 프로젝트의 일부가 되었습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

