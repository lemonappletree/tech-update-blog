# 🛠️ 2025-10-10 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Headlamp Plugin for Karpenter - Scaling and Visibility
이 기술 블로그 글은 Karpenter를 위한 Headlamp 플러그인을 소개합니다. Headlamp는 오픈 소스 Kubernetes UI 프로젝트로, 클러스터 자원을 탐색, 관리, 디버그할 수 있도록 설계되었습니다. Karpenter는 Kubernetes 자동 스케일링을 위한 노드 프로비저닝 프로젝트로, 클러스터가 빠르고 효율적으로 확장할 수 있도록 지원합니다. 새로운 Headlamp Karpenter 플러그인은 Headlamp UI에서 Karpenter의 활동을 실시간으로 가시화합니다. 이를 통해 Karpenter 자원과 Kubernetes 객체의 관계를 보여주고, 라이브 메트릭을 제공하며, 스케일링 이벤트를 실시간으로 확인할 수 있습니다. 이 플러그인은 LFX 멘토 프로젝트의 일환으로 개발되었습니다.

주요 기능으로는 Karpenter와 Kubernetes 자원의 관계를 한눈에 볼 수 있는 맵 뷰, Karpenter 메트릭 시각화, 스케일링 결정에 대한 이해와 디버깅 지원, 구성 편집기, 실시간 Karpenter 자원 뷰, 그리고 처리되지 않은 파드의 대시보드가 있습니다. 다양한 Karpenter 제공자와의 호환성도 설명되어 있으며, 사용 방법과 피드백을 위한 안내도 제공됩니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)

## 🔹 Spring Boot - Spring Batch 6.0.0-M4 released
Spring Batch 6.0.0-M4 버전이 Maven Central에서 출시되었습니다. 이번 마일스톤 릴리스의 주요 변경 사항은 jSpecify를 활용한 널 안정성 검사로의 전환과 도메인 모델 설계의 개선입니다. jSpecify 주석을 통해 코드는 컴파일 시점에 널 관련 문제를 발견할 수 있어 더 견고하고 신뢰성 있는 애플리케이션 개발이 가능합니다. 또한, 도메인 개념의 캡슐화와 명확한 관심사 분리를 통해 Spring Batch의 핵심 구성 요소를 이해하고 작업하기 더 쉽게 개선되었습니다. 추가적인 피드백은 GitHub 또는 X를 통해 받을 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/09/spring-batch-6-0-0-m4-released)

## 🔹 Docker - LoRA Explained: Faster, More Efficient Fine-Tuning with Docker
이 블로그 글은 LoRA(Low-Rank Adaptation)를 활용하여 언어 모델을 더 빠르고 효율적으로 미세 조정하는 방법을 설명합니다. 이전 글에서는 Docker Offload와 Unsloth를 사용하여 작은 로컬 모델을 효율적으로 훈련하는 방법을 다뤘습니다. 이번 글에서는 모델을 모든 작업에 능숙하게 만들기보다는 특정 작업에 특화시킬 수 있는 방법에 대해 중점적으로 설명합니다. Docker의 친숙한 워크플로우를 활용하여 모델을 보다 전문적으로 미세 조정하는 과정을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/lora-explained/)

## 🔹 Java - “Just Make All Exceptions Unchecked” - Live Q&amp;A from Devoxx
이 기술 블로그 글은 Java의 오류 처리가 예외를 중심으로 이루어지며, 특히 체크 예외와 언체크 예외의 차이점에 대해 다룹니다. 많은 Java 개발자들이 체크 예외의 복잡함 때문에 언체크 예외를 선호하게 되었고, 체크 예외가 실수였는지에 대한 의문을 가지게 된다고 합니다. 이 글에서는 Stuart Marks와 Nicolai Parlog가 이러한 주제에 대해 논의한 내용을 소개합니다.
👉 [자세히 보기](https://inside.java/2025/10/09/devoxxstream/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구 상자에 새로운 도구인 '플라이트 레코더'가 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 문제 해결과 성능 분석에 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
블로그 글 요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마무리 단계에 접어들면서, 현재 진행 상황과 커뮤니티가 참여할 수 있는 방법에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

