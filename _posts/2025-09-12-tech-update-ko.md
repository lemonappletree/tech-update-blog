# 🛠️ 2025-09-12 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Mutable CSI Node Allocatable Graduates to Beta
Kubernetes v1.34 버전에서는 CSI 드라이버가 노드의 볼륨 부착 가능 수를 업데이트할 수 있는 기능이 베타로 승격되었습니다. 이 기능은 이전에 v1.33에서 알파로 도입되었으며, 최신 노드 용량 정보를 기반으로 상태 저장 파드 스케줄링의 정확성을 향상시킵니다. 기존에는 CSI 드라이버가 정적인 최대 볼륨 부착 한도를 보고했지만, 이번 기능을 통해 런타임에서 동적으로 노드의 부착 용량을 조정하고 보고할 수 있게 되었습니다. 이러한 업데이트는 주기적 또는 자원 고갈 오류 발생 시 즉시 수행되며, 이를 통해 파드가 생성 중 상태에 영구적으로 머무르는 문제를 방지합니다. 이 기능을 사용하려면 특정 컴포넌트에서 기능 게이트를 활성화해야 하며, CSI 드라이버 설정을 통해 주기적인 업데이트를 구성할 수 있습니다. Kubernetes 커뮤니티는 사용자 피드백을 환영하며, 앞으로의 안정화 및 발전을 위해 지속적인 논의를 진행할 예정입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/11/kubernetes-v1-34-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - A Bootiful Podcast: Purnima Padmanabhan, General Manager, Tanzu Division, Broadcom
블로그 글은 "A Bootiful Podcast" 시리즈의 일환으로, Tanzu 부문의 총괄 매니저인 Purnima Padmanabhan과의 인터뷰 내용을 다루고 있습니다. 이번 에피소드에서는 AI, 플랫폼의 강점 등 다양한 주제에 대해 논의했습니다. 이 인터뷰는 SpringOne 2025 행사에서 라이브로 녹음되었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/11/a-bootiful-podcast-purnima-padmanabhan)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
이 기술 블로그 글은 AI 에이전트를 안전하게 구축하기 위해 개발자들이 런타임 보안을 어떻게 적용하고 있는지 설명합니다. AI 워크플로우가 공격 표면이 될 수 있다는 점에 주목하며, 예를 들어 LLM을 사용하여 Dockerfile이나 셸 스크립트를 생성하고 실행할 때 발생할 수 있는 위협을 다룹니다. 이러한 과정에서 발생할 수 있는 예측 불가능성과 취약성 문제를 해결하기 위해 런타임 보안의 중요성을 강조합니다.
👉 [자세히 보기](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
이 기술 블로그 글은 Java 21부터 Java 25까지의 모든 API 추가 사항에 대해 설명합니다. 주요 추가 기능으로는 범위 값, 스트림 수집기, 클래스 파일 API, 외부 함수 및 메모리 API, Javadoc 추가 기능 등이 있습니다. Java의 최신 버전에서 어떤 새로운 기능들이 도입되었는지를 자세히 알고 싶다면 이 글을 참고하면 좋습니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
제목: 새로운 실험적 Go JSON API

요약: Go 1.25에서는 새로운 실험적 지원으로 encoding/json/jsontext 및 encoding/json/v2 패키지를 도입했습니다. 이 패키지들은 JSON 처리 기능을 확장하고 개선하는 데 중점을 두고 있습니다.
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 위한 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

