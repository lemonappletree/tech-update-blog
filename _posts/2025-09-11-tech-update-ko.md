# 🛠️ 2025-09-11 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Use An Init Container To Define App Environment Variables
이 블로그 글에서는 Kubernetes v1.34의 새로운 기능인 Init Container를 사용하여 애플리케이션 환경 변수를 설정하는 방법을 설명합니다. 기존에는 ConfigMaps와 Secrets를 이용해 환경 변수를 설정했으나, 이는 추가적인 API 호출과 복잡성을 초래했습니다. 이제는 `EnvFiles` 기능 게이트를 사용하여 빈 디렉토리(`emptyDir`) 볼륨의 파일에서 직접 환경 변수를 로드할 수 있습니다. 이 방식은 환경 변수를 설정하는 데 있어 깔끔하고 간단한 해결책을 제공합니다. 또한, 민감한 데이터 처리 시 보안 문제에 주의해야 한다고 강조합니다. 이 기능은 애플리케이션 구성을 단순화하고 다양한 사용 사례를 지원할 수 있는 가능성을 열어줍니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/10/kubernetes-v1-34-env-files/)

## 🔹 Spring Boot - Spring Tools 4.32.0 released
Spring Tools 4.32.0 버전이 출시되었습니다. 이 버전은 Visual Studio Code, Eclipse, Theia용으로 제공되며, 유지 보수 릴리스로 버그 수정과 Eclipse 2025-09 릴리스에 대한 업데이트가 포함되어 있습니다. 현재 Spring Tools 4.x 라인에 대한 추가 유지 보수 릴리스 계획은 없습니다. 상세한 변경 사항은 릴리스 노트에서 확인할 수 있으며, 다운로드는 Spring Tools 웹사이트에서 가능합니다. 또한, Spring Tools 5 세대의 첫 릴리스는 2025년 11월 말로 예정되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/10/spring-tools-4-32-0-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
이 블로그 글은 AI 에이전트를 안전하게 구축하기 위한 런타임 보안의 중요성에 대해 다룹니다. AI 워크플로우는 강력하지만 예측 불가능하고 악용될 수 있는 잠재력을 가지고 있습니다. 예를 들어, 대형 언어 모델(LLM)을 통해 생성된 Dockerfile이나 쉘 스크립트는 처음에는 타당해 보이지만, 실제로 실행했을 때 예기치 않은 보안 위협이 발생할 수 있습니다. 개발자들은 이러한 문제를 방지하기 위해 런타임 보안을 워크플로우에 통합하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
블로그 글 요약: 이 글은 Java 21부터 Java 25까지 추가된 모든 API에 대해 다루고 있습니다. 주요 내용으로는 스코프 값, 스트림 수집기, 클래스 파일 API, 외부 함수 및 메모리 API, Javadoc 추가 사항 등이 포함됩니다. 이러한 API의 변화와 기능 향상에 대해 자세히 알아볼 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
블로그 글은 Go 1.25 버전에서 실험적으로 지원하는 새로운 JSON API에 관한 내용입니다. 이 버전에서는 `encoding/json/jsontext`와 `encoding/json/v2` 패키지를 소개하며, JSON 처리의 효율성과 기능성을 개선하기 위한 다양한 기능을 제공합니다. 해당 패키지들은 개발자들이 JSON 데이터를 더 쉽게 다루고, 성능을 최적화할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 향한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

