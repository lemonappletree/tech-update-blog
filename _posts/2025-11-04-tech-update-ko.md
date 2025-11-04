# 🛠️ 2025-11-04 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 블로그 글은 Kubernetes를 사용할 때 피해야 할 7가지 일반적인 함정과 이를 방지하는 방법에 대해 설명합니다. 저자는 Kubernetes를 처음 사용할 때 여러 실수를 경험했으며, 이를 통해 배운 교훈을 공유하고자 합니다. 주요 함정으로는 리소스 요청 및 제한 설정을 생략하는 것, liveness 및 readiness 프로브를 과소평가하는 것, 컨테이너 로그에만 의존하는 것, 개발 및 프로덕션 환경을 동일하게 취급하는 것, 오래된 리소스를 방치하는 것, 네트워킹에 너무 깊이 들어가는 것, 보안 및 RBAC 설정을 소홀히 하는 것이 포함됩니다. 각 함정에 대해 발생 가능한 문제점과 이를 피하는 방법을 제시하며, 실전 경험을 통해 얻은 교훈도 함께 공유합니다. Kubernetes의 강력한 기능을 제대로 활용하기 위해서는 이러한 함정을 피하고, 학습을 통해 Kubernetes의 작동 방식을 깊이 이해하는 것이 중요하다고 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Spring AI 1.1.0-M4 Available Now
Spring AI 1.1.0-M4 버전이 출시되었습니다. 이번 패치 릴리스는 안정성 향상과 버그 수정을 포함하며, 340개의 개선사항, 버그 수정, 문서 업데이트가 포함되었습니다. 주요 개선 사항으로는 35개의 기능 확장, 132개의 버그 수정, 41개의 문서 개선이 있습니다. 또한, 모델 컨텍스트 프로토콜(MCP) 업데이트, 어드바이저 실행 기능 개선, OpenAI 파일 API 통합 등 주요 기능 영역에서의 개선이 이루어졌습니다. 앞으로 Spring AI 팀은 Spring Boot를 통한 AI 애플리케이션 개발을 계속해서 개선할 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/03/spring-ai-1-1-0-M4-available-now)

## 🔹 Docker - How to Use Multimodal AI Models With Docker Model Runner
이 기술 블로그 글은 도커 모델 러너를 사용하여 멀티모달 AI 모델을 활용하는 방법에 대해 설명하고 있습니다. 멀티모달 AI는 텍스트, 이미지, 오디오 등 다양한 유형의 입력을 이해하고 생성할 수 있는 능력을 가진 최신 AI 기술 중 하나입니다. 이러한 모델을 사용하면 단순히 텍스트 입력에만 의존하지 않고 이미지나 소리를 통해서도 모델과 상호작용할 수 있습니다. 이 글에서는 이러한 멀티모달 모델을 도커 환경에서 어떻게 실행하고 활용할 수 있는지를 다루고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-use-multimodel-ai-with-model-runner/)

## 🔹 Java - Quality Outreach Heads-up - JDK 25: Consistent Behavior of ‘new File(“”)’
블로그 글 요약: "Quality Outreach Heads-up - JDK 25: ‘new File(“”)’의 일관된 동작"이라는 제목의 이 글은 JDK 25에서 빈 경로로 생성된 `File` 인스턴스의 동작 변화에 대해 설명하는 내용입니다. 이 변경 사항은 관련 프로젝트에 정기적으로 전달되는 소통의 일환으로 다뤄지고 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/03/quality-heads-up/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 'Green Tea'가 포함되었습니다. 이 블로그 글은 Green Tea 가비지 컬렉터의 특징과 작동 방식을 설명합니다. Green Tea는 메모리 관리의 효율성을 높이고, 프로그램의 성능을 향상시키기 위해 설계되었습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

