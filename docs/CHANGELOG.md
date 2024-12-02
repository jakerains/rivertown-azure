# Changelog

## [0.3.1] - 2024-03-20

### Added
- Added centralized Bland AI script configuration in settings.py
- Added enhanced call script with better structure and guidelines
- Added specific opening and closing statements for calls

### Changed
- Moved Bland AI script from bland_utils.py to settings.py
- Enhanced call script with more detailed instructions
- Improved customer service conversation flow

## [0.3.0] - 2024-03-20

### Added
- Integrated Bland AI for customer service calls
- Added customer service mode with phone number handling
- Added Sara as customer service specialist
- Added automatic call initiation system
- Added fallback phone number for technical issues

### Changed
- Updated system prompt to include customer service scenarios
- Enhanced chat flow to handle call requests
- Added session state management for CS mode
- Improved error handling for call system

## [0.2.2] - 2024-03-20

### Added
- Added Virtual Ball Designer integration to system prompt
- Added custom ball design recommendation capability
- Added link to ball designer tool (https://rivertownball-generator.netlify.app)

## [0.2.1] - 2024-03-20

### Added
- Added intelligent paragraph breaking based on sentence context
- Added special formatting for transition words and list items
- Added guidelines for concise responses in system prompt

### Changed
- Improved text formatting with smarter paragraph breaks
- Enhanced list formatting with better spacing
- Updated system prompt to encourage shorter, clearer responses
- Refined sentence handling based on length and content

## [0.2.0] - 2024-03-20

### Added
- Added smart response formatting for better readability
- Added sentence-by-sentence streaming for more natural responses
- Added improved spacing and line breaks for lists and paragraphs
- Added enhanced CSS styling for chat messages

### Changed
- Updated loading message to "Crafting the perfect response for you... 🎯"
- Improved response streaming with more natural timing
- Enhanced text formatting with proper spacing after punctuation
- Updated chat message styling with better line height and margins

## [0.1.9] - 2024-03-20

### Fixed
- Corrected spelling of "Artisanal" in company tagline
- Updated About Us text to correctly reflect 1985 founding date

## [0.1.8] - 2024-03-20

### Changed
- Set sidebar to start collapsed by default
- Enhanced menu button with better visibility and "Menu" label
- Added custom styling for menu button to match theme
- Improved menu button hover effects

## [0.1.7] - 2024-03-20

### Changed
- Updated company tagline to "Crafting Premium Artisinal Balls Since 1985!"

## [0.1.6] - 2024-03-20

### Added
- Added custom CSS styling with warm color scheme
- Added sidebar with chat controls and company info
- Added company tagline and centered header
- Added reset chat functionality

### Changed
- Updated layout to wide format
- Enhanced chat message styling with rounded corners and transparency
- Updated input field styling to match theme
- Modified welcome message to be more concise
- Improved overall visual consistency

## [0.1.5] - 2024-03-20

### Added
- Added custom chat icons for assistant (brown circle) and user
- Implemented streaming-style response display
- Added typing indicator (cursor) during response generation

### Changed
- Updated chat message display to use brand-consistent avatars
- Enhanced response visualization with word-by-word display
- Improved user experience with animated responses

## [0.1.4] - 2024-03-20

### Changed
- Updated app title to "RiverTown's Artisanal Products Chat"
- Enhanced welcome message with more enthusiastic and warm tone
- Modified chat input placeholder to be more inviting
- Updated loading spinner message to be more engaging
- Aligned all UI text with the enthusiastic product specialist persona

## [0.1.3] - 2024-03-20

### Added
- Integrated intent_mapping.prompty for better query understanding
- Combined system prompt with grounded chat prompt

### Changed
- Modified chat_with_products to use both prompts
- Added lower temperature for intent mapping
- Improved document retrieval with intent-based context

## [0.1.2] - 2024-03-20

### Added
- Created settings.py with centralized configuration
- Added temperature and max_tokens parameters to chat completion

### Changed
- Updated riverchat.py to use settings from settings.py
- Modified system prompt to use centralized configuration

## [0.1.1] - 2024-03-20

### Changed
- Moved system prompts and UI settings to separate settings.py file
- Changed app icon from football to brown circle
- Refactored UI text to use centralized settings

## [0.1.0] - 2024-03-20

### Added
- Created Streamlit-based chat interface for Rivertown Ball Company
- Added session state management for chat history
- Integrated existing chat_with_products functionality with Streamlit UI
- Added user-friendly chat interface with message history
- Added loading spinner during response generation
- Added welcome message and company branding

### Technical Details
- Uses Streamlit's chat_input and chat_message components
- Maintains chat history in session state
- Preserves context between messages
- Integrated with existing Azure AI infrastructure 