# 🛠️ 2025-11-07 기술 업데이트 요약

## 🔹 Kubernetes - Gateway API 1.4: New Features
Gateway API 1.4는 Kubernetes 네트워킹을 개선하는 새로운 기능들을 도입했습니다. 이 버전은 TLS 설정을 위한 BackendTLSPolicy, GatewayClass의 지원 기능을 명시하는 supportedFeatures, 그리고 라우트에 이름을 지정하는 규칙들을 추가하였습니다. 또한, 서비스 메쉬 구성을 위한 Mesh 리소스, 기본 게이트웨이, HTTPRoute를 위한 외부 인증 필터와 같은 실험적 기능들도 소개되었습니다. 이러한 업데이트는 Kubernetes 환경에서의 서비스 네트워킹을 더욱 유연하게 만들어 줍니다. Gateway API는 Kubernetes 1.26 이상에서 사용할 수 있으며, 여러 구현체들이 이미 이 버전을 지원하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)

## 🔹 Spring Boot - A Bootiful Podcast: The Vaadin team, live from Vaadin Create 2025
이 블로그 글은 2025년 독일 프랑크푸르트에서 열린 Vaadin Create 2025 행사에서 Vaadin 팀의 중요한 인물들인 Joonas Lehtinen, Marcus Hellberg, Leif Åstrand와 함께한 팟캐스트 에피소드를 소개합니다. 이 팟캐스트에서의 대화를 통해 Vaadin의 최신 동향과 기술에 대해 논의했습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/06/a-bootiful-podcasd-vaadin-team)

## 🔹 Docker - Dynamic MCPs with Docker: Stop Hardcoding Your Agents’ World
이 기술 블로그 글에서는 Docker를 사용한 동적 MCPs에 대해 설명하고 있습니다. MCP 프로토콜이 출시된 지 거의 1년이 되는 시점에서, 개발자들은 수천 개의 새로운 MCP 서버를 구축했습니다. 6개월 전만 해도 대부분의 개발자들은 소수의 로컬 MCP 서버를 사용하며 몇 가지 도구만을 제공했지만, 이제는 수천 개의 서버에 접근할 수 있게 되었습니다. 이 글은 에이전트의 환경을 하드코딩하지 않고 유연성을 높이는 방법에 대해 논의합니다.
👉 [자세히 보기](https://www.docker.com/blog/dynamic-mcps-stop-hardcoding-your-agents-world/)

## 🔹 Java - Try the New Valhalla EA Build - Inside Java Newscast #100
제목: 새로운 Valhalla EA 빌드를 시도하세요 - Inside Java Newscast #100

요약: JEP 401, 값 클래스와 객체가 최근 "후보" 상태로 다시 돌아왔으며, 출시를 목표로 준비 중입니다. 이를 준비하기 위해 Project Valhalla는 Java에서 정체성이 없는 값 클래스를 실험할 수 있는 새로운 얼리 액세스 빌드를 공개했습니다. 값 클래스는 정체성이 없기 때문에 개발자에게 가독성과 유지보수 측면에서 이점을 제공할 뿐만 아니라, Java 런타임에 더 많은 최적화를 위한 공간도 제공합니다. 현재 스칼라화와 일부 힙 평탄화가 가능하며, 앞으로 더 많은 최적화가 계획되어 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/06/newscast-100/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 Green Tea가 포함되었습니다. 이 가비지 컬렉터는 메모리 관리 효율성을 높이고 성능을 개선하는 데 중점을 두고 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

