# 🛠️ 2025-09-09 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: VolumeAttributesClass for Volume Modification GA
Kubernetes v1.34에서는 볼륨 속성을 동적으로 수정할 수 있는 VolumeAttributesClass API가 정식 출시(GA)되었습니다. 이는 Kubernetes 내에서 지속 가능한 스토리지를 직접 조정할 수 있는 안정적이고 강력한 방법을 제공합니다. VolumeAttributesClass는 클러스터 범위의 리소스로, 볼륨의 변경 가능한 매개변수 집합을 정의합니다. 이를 통해 사용자는 PersistentVolumeClaim(PVC)에 원하는 속성의 클래스를 지정할 수 있으며, Container Storage Interface(CSI)를 통해 이러한 변경 사항이 스토리지 시스템에 적용됩니다.

GA 버전에서는 불가능한 볼륨 수정 작업을 취소하고 이전 상태로 되돌리는 기능과 특정 VolumeAttributesClass에 대한 PersistentVolumeClaim의 할당량을 설정하는 기능이 추가되었습니다. Amazon EBS 및 Google Compute Engine Persistent Disk 등의 드라이버는 이러한 기능을 지원합니다. 더 자세한 정보는 Kubernetes 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/08/kubernetes-v1-34-volume-attributes-class/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
이 블로그 글은 SpringOne 2025 행사에서 Spring Cloud 기여자인 Ryan Baxter와의 인터뷰를 다루고 있습니다. Spring 팬들을 대상으로 한 이 팟캐스트 에피소드에서는 Ryan Baxter의 기여와 Spring Cloud에 대한 이야기를 나누고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker Inc.는 AI 애플리케이션 보안을 위해 설립된 MCP Defender를 인수했다고 발표했습니다. AI 기술의 급속한 발전은 소프트웨어 개발에 큰 변화를 가져왔으며, 이에 따라 새로운 기술이 새로운 보안 문제를 발생시킬 수 있습니다. Docker는 이번 인수를 통해 AI와 클라우드 네이티브 개발 도구, 인프라 및 서비스 분야에서의 보안 문제를 해결하려고 합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - JDK 25 G1/Parallel/Serial GC changes
JDK 25 RC 1이 출시되었으며, OpenJDK의 이번 릴리스에서 스톱-더-월드(Stop-the-world) 가비지 컬렉터에 대한 변경 사항을 간단히 소개합니다. 주요 변경 사항은 G1, 병렬(Parallel), 직렬(Serial) 가비지 컬렉터에 대한 업데이트입니다.
👉 [자세히 보기](https://inside.java/2025/09/08/jdk25-gc-changes/)

## 🔹 Golang - Testing Time (and other asynchronicities)
이 블로그 글은 비동기 코드 테스트와 `testing/synctest` 패키지에 대한 내용을 다루고 있습니다. 이는 GopherCon Europe 2025에서 같은 제목으로 발표된 내용을 바탕으로 하고 있습니다. 비동기 코드의 테스트 방법과 관련 패키지의 활용법에 대해 논의합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
Debian/Ubuntu에서 Apt를 통해 Helm을 설치하는 경우, Helm Apt 리포지토리가 이전된다는 점을 주의해야 합니다. 이전에는 Balto에서 호스팅되었으나, 이제 Buildkite에서 호스팅됩니다. 새로운 설치 지침을 참조하여 APT 키와 리포지토리 참조를 업데이트하세요.
👉 [자세히 보기](https://helm.sh/blog/debian-helm-repository-move/)

