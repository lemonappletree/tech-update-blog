# 🛠️ 2025-07-09 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 기술 블로그 글은 Kubernetes에서 GPU와 같은 특수 하드웨어를 사용하는 파드의 실패 모드를 관리하는 것의 복잡성에 대해 논의합니다. AI/ML 워크로드가 증가하면서, 이러한 워크로드는 특수 하드웨어에 의존하게 되었고, 하드웨어의 실패는 성능 저하와 중단을 초래할 수 있습니다. Kubernetes는 이러한 하드웨어 실패를 효과적으로 처리할 수 있는 지원이 부족하며, 이는 워크로드의 복잡성과 맞물려 다양한 실패 모드를 초래할 수 있습니다. 블로그에서는 Kubernetes의 기존 실패 처리 모델이 AI/ML 워크로드에 비해 부족한 점을 지적하며, Kubernetes가 여전히 AI/ML 워크로드의 선호 플랫폼인 이유와 함께, 여러 실패 모드에 대한 현재의 상태와 DIY 솔루션, 그리고 향후 로드맵을 제시합니다. Kubernetes 커뮤니티는 이러한 도전 과제를 해결하고자 지속적으로 발전하고 있으며, AI/ML 워크로드의 신뢰성과 복원력을 보장하기 위한 방향으로 나아가고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - This Week in Spring - July 8th, 2025
이번 주 Spring 블로그 글에서는 필자가 프랑스령 폴리네시아의 보라보라섬에서 파트너와 함께한 멋진 시간을 마치고 돌아와 다양한 소식을 전합니다. 주요 내용은 다음과 같습니다:

- Spring gRPC 0.9.0이 출시되었습니다.
- 지난 주 "A Bootiful Podcast"에서 전설적인 Dr. Heinz Kabutz와의 대화를 나누었습니다.
- Andres Almiray는 Spring AI와 Oracle Autonomous DB 연결에 관한 후속 블로그를 작성했습니다.
- Spring Boot 4.0의 새로운 기능을 다룬 블로그 글이 있습니다.
- AWS 개발자 옹호자인 James Ward와 함께 AI를 탐구하는 영상이 공개되었습니다.
- JUnit 6.0.0.M1이 테스트를 위해 출시되었습니다.
- Spring Modulith 2.0의 이벤트 발행 레지스트리 지원 개편에 관한 Oliver Drotbohm의 논의가 있습니다.
- JetBrains IntelliJ IDEA의 Spring Debugger에 관한 글이 올라왔습니다.
- Wim Deblauwe가 작성한 프로덕션 준비 완료된 Spring Boot 애플리케이션 작성법에 관한 블로그 글이 있습니다. 

더 많은 정보는 블로그 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/08/this-week-in-spring-july-8th-2025)

## 🔹 Docker - Introducing Docker Hub MCP Server: A New Way to Discover, Inspect, and Manage Container Images
Docker Hub는 전 세계 개발자들에게 필수적인 자원이 되었으며, 매달 110억 건의 이미지 다운로드와 1,400만 개 이상의 컨테이너 이미지를 호스팅하고 있습니다. 에이전틱 AI의 확산으로 개발자들의 작업 방식에 큰 변화가 일어나고 있으며, 점점 더 많은 개발자들이 AI 에이전트와 자동화된 워크플로우를 지원하기 위해 MCP(Model Context Protocol) 서버를 활용하고 있습니다. Docker Hub MCP 서버는 이러한 변화를 지원하는 새로운 기능을 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hub-mcp-server/)

## 🔹 Java - Marshalling: Data-Oriented Serialization
이 기술 블로그 글은 Java 언어의 최근 개선 사항과 변경된 요구 사항 및 제약 조건이 객체의 구조를 프로그래밍적으로 이해하는 데 있어 어떻게 더 간단하고 안전한 모델을 제공할 수 있는지를 설명합니다. 또한 상태 추출, 인코딩 및 재구성에 있어 더 큰 유연성을 제공하는 방법도 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/07/08/javaone-marshalling/)

## 🔹 Golang - Generic interfaces
블로그 글 "Generic interfaces"는 인터페이스 타입에 타입 매개변수를 추가하는 것이 예상보다 강력하다는 점을 설명합니다. 이를 통해 코드의 재사용성과 유연성이 크게 향상되며, 다양한 타입에 대해 보다 일반화된 인터페이스를 정의할 수 있습니다. 이 글은 Go 언어에서 제네릭 인터페이스를 활용하는 방법과 그 장점을 소개합니다.
👉 [자세히 보기](https://go.dev/blog/generic-interfaces)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 팀의 유지 보수자들과의 토론 세션과 Helm 부스에서의 만남에 참여해 보세요. 자세한 활동 내용은 블로그 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

