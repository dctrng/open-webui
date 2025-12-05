from enum import Enum


class MESSAGES(str, Enum):
    DEFAULT = lambda msg="": f"{msg if msg else ''}"
    MODEL_ADDED = lambda model="": f"The model '{model}' has been added successfully."
    MODEL_DELETED = (
        lambda model="": f"The model '{model}' has been deleted successfully."
    )


class WEBHOOK_MESSAGES(str, Enum):
    DEFAULT = lambda msg="": f"{msg if msg else ''}"
    USER_SIGNUP = lambda username="": (
        f"New user signed up: {username}" if username else "New user signed up"
    )


class ERROR_MESSAGES(str, Enum):
    def __str__(self) -> str:
        return super().__str__()

    DEFAULT = (
        lambda err="": f'{"Something went wrong :/" if err == "" else "[ERROR: " + str(err) + "]"}' + " - Đã xảy ra lỗi :/"
    )
    ENV_VAR_NOT_FOUND = "Required environment variable not found. Terminating now. - Biến môi trường bắt buộc không tìm thấy. Dừng tác vụ."
    CREATE_USER_ERROR = "Oops! Something went wrong while creating your account. Please try again later. If the issue persists, contact support for assistance. - Rất tiếc! Đã xảy ra lỗi khi tạo tài khoản của bạn. Vui lòng thử lại sau. Nếu sự cố vẫn tiếp diễn, vui lòng liên hệ bộ phận hỗ trợ để được trợ giúp."
    DELETE_USER_ERROR = "Oops! Something went wrong. We encountered an issue while trying to delete the user. Please give it another shot. - Rất tiếc! Đã xảy ra lỗi. Chúng tôi gặp sự cố khi cố gắng xóa người dùng. Vui lòng thử lại lần nữa."
    EMAIL_MISMATCH = "Uh-oh! This email does not match the email your provider is registered with. Please check your email and try again. - Rất tiếc! Email này không khớp với email mà nhà cung cấp của bạn đã đăng ký. Vui lòng kiểm tra email của bạn và thử lại."
    EMAIL_TAKEN = "Uh-oh! This email is already registered. Sign in with your existing account or choose another email to start anew. - Rất tiếc! Email này đã được đăng ký. Vui lòng đăng nhập bằng tài khoản hiện có của bạn hoặc chọn một email khác để bắt đầu lại."
    USERNAME_TAKEN = (
        "Uh-oh! This username is already registered. Please choose another username." + " - Rất tiếc! Tên người dùng này đã được đăng ký. Vui lòng chọn một tên người dùng khác."
    )
    PASSWORD_TOO_LONG = "Uh-oh! The password you entered is too long. Please make sure your password is less than 72 bytes long. - Rất tiếc! Mật khẩu bạn nhập quá dài. Vui lòng đảm bảo mật khẩu của bạn có độ dài dưới 72 byte."
    COMMAND_TAKEN = "Uh-oh! This command is already registered. Please choose another command string. - Rất tiếc! Lệnh này đã được đăng ký. Vui lòng chọn một chuỗi lệnh khác."
    FILE_EXISTS = "Uh-oh! This file is already registered. Please choose another file. - Rất tiếc! Tệp này đã được đăng ký. Vui lòng chọn một tệp khác."

    ID_TAKEN = "Uh-oh! This id is already registered. Please choose another id string. " + "- Rất tiếc! ID này đã được đăng ký. Vui lòng chọn một chuỗi ID khác."
    MODEL_ID_TAKEN = "Uh-oh! This model id is already registered. Please choose another model id string. - Rất tiếc! ID mô hình này đã được đăng ký. Vui lòng chọn một chuỗi ID mô hình khác."
    NAME_TAG_TAKEN = "Uh-oh! This name tag is already registered. Please choose another name tag string. - Rất tiếc! Thẻ tên này đã được đăng ký. Vui lòng chọn một chuỗi thẻ tên khác."
    MODEL_ID_TOO_LONG = "The model id is too long. Please make sure your model id is less than 256 characters long. - ID mô hình quá dài. Vui lòng đảm bảo ID mô hình của bạn có độ dài dưới 256 ký tự."

    INVALID_TOKEN = (
        "Your session has expired or the token is invalid. Please sign in again." + " - Phiên của bạn đã hết hạn hoặc mã thông báo không hợp lệ. Vui lòng đăng nhập lại."
    )
    INVALID_CRED = "The email or password provided is incorrect. Please check for typos and try logging in again. - Email hoặc mật khẩu được cung cấp không chính xác. Vui lòng kiểm tra lỗi chính tả và thử đăng nhập lại."
    INVALID_EMAIL_FORMAT = "The email format you entered is invalid. Please double-check and make sure you're using a valid email address (e.g., yourname@example.com). - Định dạng email bạn nhập không hợp lệ. Vui lòng kiểm tra kỹ và đảm bảo bạn đang sử dụng địa chỉ email hợp lệ (ví dụ: yourname@example.com)."
    INCORRECT_PASSWORD = (
        "The password provided is incorrect. Please check for typos and try again." + " - Mật khẩu được cung cấp không chính xác. Vui lòng kiểm tra lỗi chính tả và thử lại."
    )
    INVALID_TRUSTED_HEADER = "Your provider has not provided a trusted header. Please contact your administrator for assistance. - Nhà cung cấp của bạn chưa cung cấp tiêu đề đáng tin cậy. Vui lòng liên hệ với quản trị viên của bạn để được hỗ trợ."

    EXISTING_USERS = "You can't turn off authentication because there are existing users. If you want to disable WEBUI_AUTH, make sure your web interface doesn't have any existing users and is a fresh installation." + " - Bạn không thể tắt xác thực vì có những người dùng hiện có. Nếu bạn muốn tắt WEBUI_AUTH, hãy đảm bảo giao diện web của bạn không có người dùng hiện có và là một cài đặt mới."

    UNAUTHORIZED = "401 Unauthorized - 401 Không được ủy quyền"
    ACCESS_PROHIBITED = "You do not have permission to access this resource. Please contact your administrator for assistance. - Bạn không có quyền truy cập tài nguyên này. Vui lòng liên hệ với quản trị viên của bạn để được hỗ trợ."
    ACTION_PROHIBITED = (
        "The requested action has been restricted as a security measure." + " - Hành động được yêu cầu đã bị hạn chế như một biện pháp bảo mật."
    )

    FILE_NOT_SENT = "FILE_NOT_SENT - TỆP CHƯA ĐƯỢC GỬI"
    FILE_NOT_SUPPORTED = "Oops! It seems like the file format you're trying to upload is not supported. Please upload a file with a supported format and try again." + " - Rất tiếc! Có vẻ như định dạng tệp bạn đang cố tải lên không được hỗ trợ. Vui lòng tải lên một tệp có định dạng được hỗ trợ và thử lại."

    NOT_FOUND = "We could not find what you're looking for :/ - Chúng tôi không tìm thấy những gì bạn đang tìm kiếm :/"
    USER_NOT_FOUND = "We could not find what you're looking for :/ - Chúng tôi không tìm thấy những gì bạn đang tìm kiếm :/"
    API_KEY_NOT_FOUND = "Oops! It looks like there's a hiccup. The API key is missing. Please make sure to provide a valid API key to access this feature." + " - Rất tiếc! Có vẻ như có một sự cố. Khóa API bị thiếu. Vui lòng đảm bảo cung cấp khóa API hợp lệ để truy cập tính năng này."
    API_KEY_NOT_ALLOWED = "Use of API key is not enabled in the environment. - Việc sử dụng khóa API không được bật trong môi trường."

    MALICIOUS = "Unusual activities detected, please try again in a few minutes. - Phát hiện hoạt động bất thường, vui lòng thử lại sau vài phút."

    PANDOC_NOT_INSTALLED = "Pandoc is not installed on the server. Please contact your administrator for assistance. - Pandoc chưa được cài đặt trên máy chủ. Vui lòng liên hệ với quản trị viên của bạn để được hỗ trợ."
    INCORRECT_FORMAT = (
        lambda err="": f"Invalid format. Please use the correct format{err}" + " - Định dạng không hợp lệ. Vui lòng sử dụng đúng định dạng."
    )
    RATE_LIMIT_EXCEEDED = "API rate limit exceeded - Quá giới hạn API."

    MODEL_NOT_FOUND = lambda name="": f"Model '{name}' was not found" + " - Không tìm thấy mô hình."
    OPENAI_NOT_FOUND = lambda name="": "OpenAI API was not found" + " - Không tìm thấy API OpenAI."
    OLLAMA_NOT_FOUND = "WebUI could not connect to Ollama - WebUI không thể kết nối với Ollama."
    CREATE_API_KEY_ERROR = "Oops! Something went wrong while creating your API key. Please try again later. If the issue persists, contact support for assistance." + " - Rất tiếc! Đã xảy ra lỗi khi tạo khóa API của bạn. Vui lòng thử lại sau. Nếu sự cố vẫn tiếp diễn, vui lòng liên hệ bộ phận hỗ trợ để được trợ giúp."
    API_KEY_CREATION_NOT_ALLOWED = "API key creation is not allowed in the environment. - Việc tạo khóa API không được phép trong môi trường."

    EMPTY_CONTENT = "The content provided is empty. Please ensure that there is text or data present before proceeding." + " - Nội dung được cung cấp trống. Vui lòng đảm bảo có văn bản hoặc dữ liệu trước khi tiếp tục."

    DB_NOT_SQLITE = "This feature is only available when running with SQLite databases." + " - Tính năng này chỉ khả dụng khi chạy với cơ sở dữ liệu SQLite."

    INVALID_URL = (
        "Oops! The URL you provided is invalid. Please double-check and try again." + " - Rất tiếc! URL bạn cung cấp không hợp lệ. Vui lòng kiểm tra kỹ và thử lại."
    )

    WEB_SEARCH_ERROR = (
        lambda err="": f"{err if err else 'Oops! Something went wrong while searching the web.'}" + " - Rất tiếc! Đã xảy ra lỗi khi tìm kiếm trên web."
    )

    OLLAMA_API_DISABLED = (
        "The Ollama API is disabled. Please enable it to use this feature." + " - API Ollama bị tắt. Vui lòng bật nó để sử dụng tính năng này."
    )

    FILE_TOO_LARGE = (
        lambda size="": f"Oops! The file you're trying to upload is too large. Please upload a file that is less than {size}." + " - Rất tiếc! Tệp bạn đang cố tải lên quá lớn. Vui lòng tải lên một tệp có kích thước nhỏ hơn."
    )

    DUPLICATE_CONTENT = (
        "Duplicate content detected. Please provide unique content to proceed." + " - Phát hiện nội dung trùng lặp. Vui lòng cung cấp nội dung duy nhất để tiếp tục."
    )
    FILE_NOT_PROCESSED = "Extracted content is not available for this file. Please ensure that the file is processed before proceeding." + " - Nội dung được trích xuất không khả dụng cho tệp này. Vui lòng đảm bảo tệp được xử lý trước khi tiếp tục."

    INVALID_PASSWORD = lambda err="": (
        err if err else "The password does not meet the required validation criteria."
    ) + " - Mật khẩu không đáp ứng các tiêu chí xác thực bắt buộc."


class TASKS(str, Enum):
    def __str__(self) -> str:
        return super().__str__()

    DEFAULT = lambda task="": f"{task if task else 'generation'}"
    TITLE_GENERATION = "title_generation"
    FOLLOW_UP_GENERATION = "follow_up_generation"
    TAGS_GENERATION = "tags_generation"
    EMOJI_GENERATION = "emoji_generation"
    QUERY_GENERATION = "query_generation"
    IMAGE_PROMPT_GENERATION = "image_prompt_generation"
    AUTOCOMPLETE_GENERATION = "autocomplete_generation"
    FUNCTION_CALLING = "function_calling"
    MOA_RESPONSE_GENERATION = "moa_response_generation"
