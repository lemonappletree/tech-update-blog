# 🛠️ 2025-09-05 기술 업데이트 요약

## 🔹 Kubernetes - PSI Metrics for Kubernetes Graduates to Beta
이 기술 블로그 글은 Kubernetes v1.34 버전에서 Pressure Stall Information (PSI) 메트릭이 베타로 전환되었음을 알리는 내용입니다. PSI는 리눅스 커널의 기능으로, 리소스 사용량을 넘어서 작업이 리소스 경쟁으로 인해 지연되는 시간을 측정하여 리소스 병목 현상을 식별하고 진단하는 데 도움을 줍니다. Kubernetes에서는 PSI 메트릭을 통해 CPU, 메모리, I/O의 리소스 압박을 모니터링할 수 있으며, 이를 통해 성능 문제의 원인을 파악하고 해결할 수 있습니다. PSI 메트릭을 활성화하려면 Linux 커널 버전 4.20 이상과 cgroup v2를 사용해야 합니다. PSI는 Linux 커널 기능이므로 Windows 노드에서는 사용할 수 없습니다. Kubernetes 커뮤니티는 이 기능의 피드백을 기다리고 있으며, 향후 안정적인 GA 릴리스를 목표로 개선을 진행하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/04/kubernetes-v1-34-introducing-psi-metrics-beta/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
블로그 글 요약: 이번 블로그 글에서는 SpringOne 2025 행사에서 진행된 팟캐스트를 통해 뛰어난 Spring Cloud 기여자인 Ryan Baxter와의 대화를 소개합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Hybrid AI Isn’t the Future — It’s Here (and It Runs in Docker)
블로그 글에서는 하이브리드 AI의 현재와 Docker에서의 실행에 대해 다루고 있습니다. 클라우드에서 대규모 AI 모델을 실행하면 강력한 기능에 접근할 수 있지만, 그만큼 비용도 증가하며 예기치 않은 비용 발생 위험이 있습니다. 반면, 로컬 모델은 비용을 예측 가능하게 만들고 개인정보 보호를 강화하는 반면, 모델의 규모가 작아지면서 기능에 제한이 생길 수 있습니다. 이 블로그는 이러한 하이브리드 AI 접근 방식과 Docker를 활용한 실행 방안에 대해 설명하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/hybrid-ai-and-how-it-runs-in-docker/)

## 🔹 Java - The Inside Java Newsletter: Java 25, AI World, JavaOne 2026!
이 기술 블로그 글은 2025년 8월의 Inside Java 뉴스레터에 대한 요약입니다. 주요 내용은 9월에 출시될 Java 25, 10월에 열리는 Oracle AI World에서의 Java 세션, 그리고 2026년 3월에 개최될 JavaOne 발표입니다. 또한 Java 사용자 그룹, 커뮤니티 이벤트, 엔지니어링 및 커뮤니티 팟캐스트, Java 플랫폼 그룹 내 개발자들의 기술 콘텐츠에 대한 최신 업데이트를 지속적으로 제공합니다. Inside Java 뉴스레터는 Java Developer Relations 팀에서 제작하며, 개발자, 학습자, 교육자 및 고객을 위한 다양한 멀티미디어 콘텐츠는 learn.java, dev.java, inside.java에서 확인할 수 있습니다. 뉴스레터 아카이브를 확인하고 구독하여 친구에게 공유하세요.
👉 [자세히 보기](https://inside.java/2025/09/02/inside-java-newsletter/)

## 🔹 Golang - Testing Time (and other asynchronicities)
블로그 글 "Testing Time (and other asynchronicities)"는 비동기 코드 테스트와 `testing/synctest` 패키지에 대해 논의합니다. 이 글은 GopherCon Europe 2025에서 발표된 같은 제목의 강연을 바탕으로 작성되었습니다. 비동기 코드의 테스트 방법과 관련 도구에 대한 내용을 다루고 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
블로그 글 요약: Helm을 Apt로 설치하는 경우, Debian/Ubuntu Helm Apt 저장소가 이전된다는 점에 유의해야 합니다. 이전에는 Balto에서 호스팅되었으나 이제 Buildkite에서 호스팅됩니다. 새로운 설치 지침을 참조하여 APT 키와 저장소 참조를 업데이트해야 합니다.
👉 [자세히 보기](https://helm.sh/blog/debian-helm-repository-move/)

