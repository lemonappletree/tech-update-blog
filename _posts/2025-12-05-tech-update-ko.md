# 🛠️ 2025-12-05 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.35 Sneak Peek
이 기술 블로그 글에서는 Kubernetes v1.35의 예정된 변경 사항을 소개합니다. 주요 내용은 다음과 같습니다:

1. **기능 중단 및 제거**:
   - **cgroup v1 지원 중단**: Kubernetes는 cgroup v1의 지원을 중단하고 cgroup v2로 전환할 예정입니다. 이는 리눅스 노드에서 더 나은 리소스 격리를 제공하기 위함입니다.
   - **kube-proxy의 ipvs 모드 중단**: ipvs 모드는 유지 관리의 복잡성 때문에 중단됩니다. 대신 nftables 모드를 사용할 것을 권장합니다.
   - **containerd v1.y 지원 중단**: containerd v1.x의 지원이 중단되므로 v2.0 이상으로 전환해야 합니다.

2. **주요 개선 사항**:
   - **노드 선언 기능**: 노드가 지원하는 기능을 선언하여 클러스터 업그레이드 시 버전 차이로 인한 문제를 줄입니다.
   - **Pod 리소스의 인플레이스 업데이트**: Pod를 재시작하지 않고도 리소스를 조정할 수 있는 기능이 안정화됩니다.
   - **Pod 인증서**: Pod 간의 안전한 통신을 위한 인증서를 자동으로 발급하고 갱신하는 기능이 도입됩니다.
   - **수치형 태인트**: 수치 비교 연산자를 추가하여 노드의 수치적 속성을 기반으로 스케줄링을 개선합니다.
   - **사용자 네임스페이스**: 컨테이너의 root 사용자를 안전하게 리맵하여 보안을 강화합니다.
   - **OCI 이미지를 볼륨으로 마운트 지원**: OCI 레지스트리에서 데이터를 끌어와 볼륨으로 사용하는 기능이 도입됩니다.

이 외에도 Kubernetes v1.35는 2025년 12월 17일에 출시될 예정이며, 새로운 기능 및 변경 사항에 대한 자세한 내용은 공식 릴리스 노트를 통해 확인할 수 있습니다. Kubernetes 커뮤니티에 참여하여 더 많은 정보를 얻고 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)

## 🔹 Spring Boot - A Bootiful Podcast: Dan Vega on the fundamentals of software engineering
블로그 글 요약: Spring 개발자 홍보대사인 Dan Vega가 최근 출간한 책 '소프트웨어 공학의 기초'에 대해 이야기하는 팟캐스트가 소개되었습니다. 글쓴이는 Dan Vega와의 대화에 대해 매우 기대하고 있으며, 해당 책을 통해 소프트웨어 공학의 기본 원칙을 탐구할 수 있다고 설명합니다.
👉 [자세히 보기](https://spring.io/blog/2025/12/04/a-bootiful-podcast-dan-vega)

## 🔹 Docker - Securing the Docker MCP Catalog: Commit Pinning, Agentic Auditing, and Publisher Trust Levels
이 기술 블로그 글은 Docker MCP 카탈로그의 보안을 강화하는 방법에 대해 설명합니다. AI 도우미를 실제 도구에 연결할 때 신뢰가 가장 중요하며, MCP 컨테이너화는 서버의 오작동이나 침해 시 영향을 제한하는 강력한 격리를 제공합니다. Docker MCP 솔루션의 신뢰성과 보안을 지속적으로 강화하여 악성 코드 노출을 줄이고자 하며, MCP 생태계가 확장됨에 따라 보안을 더욱 강화하는 노력을 하고 있습니다. 주요 방법으로는 커밋 고정, 에이전트 감사, 발행자 신뢰 수준 등이 포함됩니다.
👉 [자세히 보기](https://www.docker.com/blog/enhancing-mcp-trust-with-the-docker-mcp-catalog/)

## 🔹 Java - All Features in Java 26 - Inside Java Newscast #102
Java 26, 또는 JDK 26이 오늘부터 램프다운 단계 1에 들어가며, 기능 세트가 확정되었습니다. 이번 버전에는 HTTP/3 지원, 성능 및 AOT(선행 컴파일) 개선, 최종 필드 변경을 관리하기 위한 새로운 명령줄 플래그가 추가되었습니다. 또한, 지속적인 프리뷰 기능의 발전이 이루어져 Java가 한 단계 더 발전했습니다.
👉 [자세히 보기](https://inside.java/2025/12/04/newscast-102/)

## 🔹 Golang - Go’s Sweet 16
Go 프로그래밍 언어의 16주년을 축하하는 내용의 기술 블로그 글입니다. Go 언어의 발전과 그 동안의 성과를 기념하며, 커뮤니티와 기여자들에게 감사의 인사를 전하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

## 🔹 Helm - Helm 4 Released
2023년 11월 12일 수요일, KubeCon + CloudNativeCon에서 열린 Helm 4 발표 중에 Helm v4.0.0이 출시되었습니다. 이는 6년 만에 출시된 Helm의 첫 번째 주요 새 버전입니다.
👉 [자세히 보기](https://helm.sh/blog/helm-4-released)

