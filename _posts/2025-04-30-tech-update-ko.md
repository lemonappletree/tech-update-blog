# 🛠️ 2025-04-30 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Image Volumes graduate to beta!
Kubernetes v1.33에서는 v1.31에서 알파 기능으로 도입된 이미지 볼륨(Image Volumes)이 베타로 승격되었습니다. 이 기능은 기본적으로 비활성화되어 있으며, 일부 컨테이너 런타임에서만 지원됩니다. 주요 업데이트로는 `subPath`와 `subPathExpr`를 통한 하위 디렉터리 마운트 지원이 추가되었으며, 새로운 kubelet 메트릭도 도입되었습니다. 사용자는 특정 이미지 볼륨의 하위 디렉터리를 읽기 전용으로 마운트할 수 있으며, 존재하지 않는 디렉터리는 기본적으로 마운트할 수 없습니다. 이 기능은 안전성을 위해 절대 경로나 상대 경로의 사용을 제한하며, 컨테이너 런타임에서도 이를 확인해야 합니다. SIG Node는 이 기능의 발전에 기여한 모든 사람들에게 감사를 표하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/29/kubernetes-v1-33-image-volume-beta/)

## 🔹 Spring Boot - This Week in Spring - April 29th, 2025
이번 주 Spring 블로그 요약:

이번 주에는 다양한 행사에 참여할 예정이며, 새로운 소식이 풍성합니다. 다음 주부터 Devoxx UK, CodeRemix Miami, 스톡홀름의 JForum #123, 바르셀로나의 Spring IO, 포르투갈의 JNation, 도쿄의 Japan Java User Group Spring 컨퍼런스에 참석합니다. 또한, 여러 새로운 릴리스가 발표되었습니다. Spring Boot 3.5.0-RC1, Spring gRPC 0.8.0, Spring Modulith 1.4 RC1 등 다양한 버전이 출시되었습니다. 팟캐스트에서는 Java 챔피언 Simon Maple과의 인터뷰가 진행되었습니다. Java 관련 비디오와 기사도 추천하고 있습니다. Spring 관련 최신 업데이트와 행사에 대한 자세한 정보는 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/29/this-week-in-spring-april-29th-2025)

## 🔹 Docker - Docker Desktop 4.41: Docker Model Runner supports Windows, Compose, and Testcontainers integrations, Docker Desktop on the Microsoft Store
Docker Desktop 4.41 버전에서는 AI 개발자와 대규모 환경을 관리하는 팀을 위한 새로운 도구들이 추가되었습니다. 이번 업데이트에는 Windows에서 Docker Model Runner를 지원하고, Compose 및 Testcontainers와의 통합 기능이 포함되어 있습니다. 또한, Docker Desktop이 Microsoft Store에서 이용 가능하게 되었습니다. 이를 통해 개발 속도를 높이고 더 효율적인 협업이 가능해졌습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-4-41/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
블로그 글 요약: Java 25 릴리스에서 Java에 큰 변화가 있을 예정입니다. 이번 Inside Java Newscast 에피소드에서는 Java 25에서 최종 확정될 예정인 'Paving the On-ramp' 기능 세트를 살펴봅니다. 또한 Java를 배우고자 하는 사람들과 Java를 가르치는 사람들을 위한 새로운 웹사이트 lear.java의 출시에 대해서도 다룹니다.
👉 [자세히 보기](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24 버전에서의 더 예측 가능한 벤치마킹을 위한 새로운 기능인 `testing.B.Loop`에 대해 설명합니다. 이 기능은 벤치마크 루핑을 개선하여 개발자들이 더 정확하고 일관된 성능 테스트를 수행할 수 있도록 돕습니다. 이를 통해 Go 언어를 사용하는 개발자들은 성능을 최적화하고 코드의 효율성을 더욱 높일 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참여합니다. 올해 말 출시 예정인 Helm 4에 대한 대화에 참여하고, 발표 세션 및 Project Pavilion의 Helm 부스에서 유지보수자들과 만날 수 있는 기회를 놓치지 마세요. 이번 주 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

